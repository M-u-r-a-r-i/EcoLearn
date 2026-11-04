// 404: any URL that matches no page (a mistyped link, an old bookmark).
// Rendered inside the root layout, so the nav — and the way home — stays.

import Link from "next/link";
import { Compass } from "lucide-react";
import { Button } from "@/components/ui/button";


export default function NotFound() {
  return (
    <main className="page-shell w-full flex-1">
      <div className="mx-auto w-full flex flex-1 flex-col items-center justify-center gap-5 text-center">
        <Compass className="size-12 text-primary" aria-hidden />
        <h1 className="display text-4xl font-semibold text-foreground">This page doesn&apos;t exist</h1>
        <p className="max-w-md text-muted-foreground">
          The link may be mistyped or out of date. Your lessons and progress are safe.
        </p>
        <div className="flex flex-wrap justify-center gap-3">
          <Button asChild>
            <Link href="/roadmap">Go to my roadmap</Link>
          </Button>
          <Link href="/" className="self-center text-sm font-semibold text-primary hover:underline">
            Home page
          </Link>
        </div>
      </div>
    </main>
  );
}
