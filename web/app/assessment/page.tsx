// Placeholder assessment page (/assessment). The real graded check (POST
// /api/assessment) comes next. For now it just gives "Take the quick check" a
// real destination instead of a 404.

"use client";

import Link from "next/link";

import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { SectionHeading } from "@/components/section-heading";

export default function AssessmentPage() {
  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-6 text-center">
        <SectionHeading
          eyebrow="Assessment"
          title="Quick check coming soon"
          subtitle="Next we'll grade your answer to the lesson's check question here."
          className="items-center text-center"
        />
        <PrimaryButton asChild>
          <Link href="/lesson">← Back to the lesson</Link>
        </PrimaryButton>
      </PageContainer>
    </main>
  );
}
