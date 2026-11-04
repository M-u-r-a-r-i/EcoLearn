// 404: any URL that matches no page (a mistyped link, an old bookmark).
// Rendered inside the root layout, so the nav — and the way home — stays.

import Link from "next/link";
import { Compass } from "lucide-react";

import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";

export default function NotFound() {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-5 text-center">
        <Compass className="size-12 text-primary" aria-hidden />
        <h1 className="text-3xl font-bold tracking-tight text-foreground">This page doesn&apos;t exist</h1>
        <p className="max-w-md text-muted-foreground">
          The link may be mistyped or out of date. Your lessons and progress are safe.
        </p>
        <div className="flex flex-wrap justify-center gap-3">
          <PrimaryButton asChild>
            <Link href="/roadmap">Go to my roadmap</Link>
          </PrimaryButton>
          <Link href="/" className="self-center text-sm font-semibold text-primary hover:underline">
            Home page
          </Link>
        </div>
      </PageContainer>
    </main>
  );
}
