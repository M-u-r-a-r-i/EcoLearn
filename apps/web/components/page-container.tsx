// A consistent content wrapper. Every page renders its content inside
// <PageContainer> so the max-width, horizontal centering, and side padding are
// identical everywhere — no page invents its own width. Pass `className` to
// tweak per page (e.g. add vertical centering) without losing the shared base.

import * as React from "react";

import { cn } from "@/lib/utils";

export function PageContainer({
  className,
  children,
}: {
  className?: string;
  children: React.ReactNode;
}) {
  return (
    <div className={cn("mx-auto w-full max-w-[1200px] px-8 pt-8 pb-20 max-md:px-4 max-md:pt-6", className)}>
      {children}
    </div>
  );
}
