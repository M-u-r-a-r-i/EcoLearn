import { notFound } from "next/navigation";
import { Suspense } from "react";

import { PreviewShell } from "@/components/preview/shell";

export function generateStaticParams() {
  return [{ dir: "a" }, { dir: "b" }, { dir: "c" }];
}

export default async function PreviewDirection({ params }: { params: Promise<{ dir: string }> }) {
  const { dir } = await params;
  if (dir !== "a" && dir !== "b" && dir !== "c") notFound();
  return (
    <Suspense fallback={null}>
      <PreviewShell dir={dir} />
    </Suspense>
  );
}
