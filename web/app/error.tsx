// A crash in any page (a bug, or a response the page didn't expect) shows this
// instead of a blank screen. It sits inside the root layout, so the nav stays.
//
// Next 16: the recovery prop is `unstable_retry` (it re-fetches and re-renders
// the segment), not `reset` — see node_modules/next/dist/docs, file-conventions/error.md.
// Network failures are mostly handled where they happen (lib/api.ts turns them
// into friendly messages); this catches what slips past that.

"use client";

import { useEffect } from "react";
import Link from "next/link";
import { RefreshCw, TriangleAlert } from "lucide-react";

import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";

export default function ErrorPage({
  error,
  unstable_retry,
}: {
  error: Error & { digest?: string };
  unstable_retry: () => void;
}) {
  useEffect(() => {
    // The browser console is the only error log on a local pilot setup.
    console.error(error);
  }, [error]);

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-5 text-center">
        <TriangleAlert className="size-12 text-brand-accent" aria-hidden />
        <h1 className="text-3xl font-bold tracking-tight text-foreground">Something went wrong</h1>
        <p className="max-w-md text-muted-foreground">
          This page hit a problem. Your progress is saved — trying again usually fixes it. If it keeps
          happening, tell your teacher.
        </p>
        {error.digest && <p className="text-xs text-muted-foreground">Reference: {error.digest}</p>}
        <div className="flex flex-wrap justify-center gap-3">
          <PrimaryButton onClick={() => unstable_retry()}>
            <RefreshCw className="size-5" /> Try again
          </PrimaryButton>
          <Link href="/roadmap" className="self-center text-sm font-semibold text-primary hover:underline">
            Go to my roadmap
          </Link>
        </div>
      </PageContainer>
    </main>
  );
}
