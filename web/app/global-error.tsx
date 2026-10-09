// The last resort: shown only if the root layout itself fails (so the nav, the
// auth provider and our styles may all be unavailable). It replaces the whole
// document, so it brings its own <html>, <body>, styles and title, and depends
// on nothing else in the app.

"use client";

export default function GlobalError({
  error,
  unstable_retry,
}: {
  error: Error & { digest?: string };
  unstable_retry: () => void;
}) {
  return (
    <html lang="en">
      <body
        style={{
          margin: 0,
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: "'Avenir Next', 'Trebuchet MS', system-ui, sans-serif",
          background: "#f4f3ed",
          color: "#202a27",
          textAlign: "center",
          padding: 16,
        }}
      >
        <title>EcoLearn — something went wrong</title>
        <div style={{ maxWidth: 420 }}>
          <h1 style={{ fontSize: 28, marginBottom: 8 }}>EcoLearn hit a problem</h1>
          <p style={{ color: "#667066", lineHeight: 1.5 }}>
            Your progress is saved. Try again, and if it keeps happening, tell your teacher.
          </p>
          {error.digest && <p style={{ fontSize: 12, color: "#667066" }}>Reference: {error.digest}</p>}
          <button
            onClick={() => unstable_retry()}
            style={{
              marginTop: 16,
              padding: "10px 20px",
              borderRadius: 13,
              border: "none",
              boxShadow: "0 5px 0 #1b5b48",
              background: "#26745d",
              color: "white",
              fontSize: 16,
              fontWeight: 600,
              cursor: "pointer",
            }}
          >
            Try again
          </button>
        </div>
      </body>
    </html>
  );
}
