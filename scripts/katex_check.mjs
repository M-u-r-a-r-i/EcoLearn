// Render every maths expression with KaTeX — the same library the web app
// uses (via rehype-katex) — and report the ones that fail.
//
// Input  (stdin):  JSON [{ "id": "...", "tex": "...", "display": true|false }, ...]
// Output (stdout): JSON [{ "id": "...", "error": "..." }, ...]   (only failures)
//
// Called by src/content/validate.py. KaTeX is resolved from web/node_modules so
// the check always uses exactly the version the student's browser gets.

import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(here, "..", "web", "package.json"));
const katex = require("katex");

let input = "";
process.stdin.setEncoding("utf8");
for await (const chunk of process.stdin) input += chunk;

const failures = [];
for (const item of JSON.parse(input)) {
  try {
    katex.renderToString(item.tex, {
      displayMode: item.display,
      throwOnError: true,
      strict: "ignore",
    });
  } catch (err) {
    failures.push({ id: item.id, error: String(err.message).split("\n")[0] });
  }
}
process.stdout.write(JSON.stringify(failures));
