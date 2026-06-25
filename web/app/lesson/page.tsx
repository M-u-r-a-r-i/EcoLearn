// Placeholder lesson page (/lesson). The real lesson (served from
// GET /api/next-lesson) comes next. For now it just gives "Continue Learning"
// a real destination instead of a 404.

"use client";

import Link from "next/link";

import { useStudent } from "@/components/student-provider";
import { PageContainer } from "@/components/page-container";
import { PrimaryButton } from "@/components/primary-button";
import { SectionHeading } from "@/components/section-heading";

export default function LessonPage() {
  const { student } = useStudent();

  return (
    <main className="flex flex-1 flex-col">
      <PageContainer className="flex flex-1 flex-col items-center justify-center gap-6 text-center">
        <SectionHeading
          eyebrow="Lesson"
          title="Lesson page coming soon"
          subtitle={
            student
              ? `Next we'll load ${student.name}'s personalised lesson here.`
              : "We'll load your personalised lesson here."
          }
          className="items-center text-center"
        />
        <PrimaryButton asChild>
          <Link href="/roadmap">← Back to roadmap</Link>
        </PrimaryButton>
      </PageContainer>
    </main>
  );
}
