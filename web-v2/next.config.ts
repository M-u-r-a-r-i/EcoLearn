import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // `next dev` only serves its dev scripts (and live reload) to the host it
  // started on, localhost. Opened at http://127.0.0.1:3000 instead, the page
  // still rendered but none of its JavaScript ran, so "Log in" just reloaded
  // the page (2026-10-02). Allow the loopback address too.
  allowedDevOrigins: ["127.0.0.1"],
};

export default nextConfig;
