// The landing page's main buttons. A visitor sees "Get started" and "Log in"; someone who is
// already signed in sees a way back to their own home instead (nothing flashes while the
// session is being checked).

"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";

import { HOME, useAuth } from "@/components/auth-provider";
import { PrimaryButton } from "@/components/primary-button";
import { Button } from "@/components/ui/button";

export function HeroActions({ stacked = false }: { stacked?: boolean }) {
  const { status, role } = useAuth();
  const layout = stacked ? "flex-col sm:flex-row" : "flex-row";

  if (status === "loading") return <div className="h-12" aria-hidden />;
  if (status === "authenticated" && role) {
    return (
      <div className={`flex flex-wrap gap-3 ${layout}`}>
        <PrimaryButton asChild>
          <Link href={HOME[role]}>
            {role === "teacher" ? "Go to my classes" : "Back to my roadmap"} <ArrowRight className="size-5" />
          </Link>
        </PrimaryButton>
      </div>
    );
  }
  return (
    <div className={`flex flex-wrap gap-3 ${layout}`}>
      <PrimaryButton asChild>
        <Link href="/signup">
          Get started <ArrowRight className="size-5" />
        </Link>
      </PrimaryButton>
      <Button variant="outline" size="lg" asChild className="h-12 rounded-xl px-6 text-base font-semibold">
        <Link href="/login">Log in</Link>
      </Button>
    </div>
  );
}
