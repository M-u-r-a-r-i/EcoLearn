"""Headless Edge over CDP: log in to the deck copy (web :3100, API :8100) and save screenshots.
Usage: python shoot.py <script.json>   where the json is a list of steps:
  {"login": "aarav.k", "kind": "student"|"teacher"}
  {"go": "/roadmap", "wait": 4}
  {"js": "...", "wait": 1}
  {"shot": "name", "full": false, "height": 900}
"""
import base64, json, os, subprocess, sys, time, urllib.request
from pathlib import Path
import websocket

HERE = Path(__file__).parent
WEB, API = "http://localhost:3100", "http://localhost:8100"
# The demo accounts' password: ECOLEARN_DEMO_PASSWORD, else the one scripts/seed_demo.py made
# (data/.demo_password). It used to be written here, which put it on GitHub.
_REPO = HERE.parents[3]
PASSWORD = os.environ.get("ECOLEARN_DEMO_PASSWORD") or (_REPO / "data" / ".demo_password").read_text().strip()
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PORT = 9333
W, H, SCALE = 1440, 900, 1.5


class Tab:
    def __init__(self):
        self.proc = subprocess.Popen([EDGE, "--headless=new", f"--remote-debugging-port={PORT}",
                                      f"--user-data-dir={HERE / 'edge-profile'}", "--hide-scrollbars",
                                      "--no-first-run", "about:blank"])
        for _ in range(50):
            try:
                pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
                page = next(p for p in pages if p["type"] == "page")
                break
            except Exception:
                time.sleep(0.3)
        self.ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=120, suppress_origin=True)
        self.n = 0
        self.cmd("Page.enable")
        self.metrics(H)

    def cmd(self, method, **params):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.n:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def metrics(self, height):
        self.cmd("Emulation.setDeviceMetricsOverride", width=W, height=height, deviceScaleFactor=SCALE, mobile=False)

    def js(self, expr):
        r = self.cmd("Runtime.evaluate", expression=expr, awaitPromise=True, returnByValue=True)
        if "exceptionDetails" in r:
            raise RuntimeError(r["exceptionDetails"].get("exception", {}).get("description", r["exceptionDetails"]))
        return r.get("result", {}).get("value")

    def go(self, path, wait=4):
        self.cmd("Page.navigate", url=WEB + path)
        time.sleep(wait)
        self.js("document.querySelectorAll('nextjs-portal').forEach(e=>e.remove()); 1")

    def shot(self, name, height=None, full=False):
        self.js("document.querySelectorAll('nextjs-portal').forEach(e=>e.remove()); 1")
        if full:
            height = int(self.js("document.documentElement.scrollHeight"))
        self.metrics(height or H)
        time.sleep(0.8)
        data = self.cmd("Page.captureScreenshot", format="png", captureBeyondViewport=bool(full))["data"]
        out = HERE / "shots" / f"{name}.png"
        out.write_bytes(base64.b64decode(data))
        self.metrics(H)
        print("saved", out.name)


def main():
    steps = json.loads(Path(sys.argv[1]).read_text())
    t = Tab()
    try:
        t.go("/", 3)
        t.js("localStorage.setItem('ecolearn-theme','light'); 1")
        for s in steps:
            if "login" in s:
                url = API + ("/api/teacher/login" if s.get("kind") == "teacher" else "/api/auth/login")
                t.js(f"fetch('{API}/api/auth/logout',{{method:'POST',credentials:'include'}}).catch(()=>0).then(()=>1)")
                status = t.js(f"fetch('{url}',{{method:'POST',credentials:'include',headers:{{'Content-Type':'application/json'}},"
                              f"body:JSON.stringify({{username:'{s['login']}',password:'{PASSWORD}'}})}}).then(r=>r.status)")
                print("login", s["login"], status)
            elif "go" in s:
                t.go(s["go"], s.get("wait", 4))
            elif "js" in s:
                print("js ->", str(t.js(s["js"]))[:2500])
                time.sleep(s.get("wait", 1))
            elif "shot" in s:
                t.shot(s["shot"], s.get("height"), s.get("full", False))
    finally:
        try:
            t.cmd("Browser.close")
        except Exception:
            pass
        t.proc.wait(timeout=10)


if __name__ == "__main__":
    main()
