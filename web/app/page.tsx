// This file IS the homepage (the "/" route). Whatever this component returns is
// what shows at http://localhost:3000/. We import the shadcn components we added
// (they live in components/ui — the "@/" is a shortcut to the web/ root) and lay
// them out with Tailwind utility classes.
//
// NOTE: this is presentation only for now — the buttons don't do anything yet.
// Wiring them to the FastAPI backend is the next step.

import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";

export default function Home() {
  return (
    // min-h-screen = fill the screen height; flex + items/justify-center = center
    // the card; the gradient + padding give it some breathing room.
    <main className="flex min-h-screen flex-col items-center justify-center gap-8 bg-gradient-to-b from-indigo-50 to-white p-6">
      {/* Hero heading */}
      <div className="text-center">
        <h1 className="text-4xl font-extrabold tracking-tight text-slate-900 sm:text-5xl">
          🌱 EcoLearn
        </h1>
        <p className="mt-3 max-w-md text-lg text-slate-600">
          Learn Class&nbsp;11 Physics through what you love.
        </p>
      </div>

      {/* Onboarding card */}
      <Card className="w-full max-w-md shadow-lg">
        <CardHeader>
          <CardTitle>Start learning</CardTitle>
          <CardDescription>
            Pick the interest we&apos;ll use to explain every concept.
          </CardDescription>
        </CardHeader>

        <CardContent className="flex gap-3">
          {/* "outline" and "default" are built-in shadcn button styles */}
          <Button variant="outline" className="flex-1">
            ⚽ Football
          </Button>
          <Button variant="outline" className="flex-1">
            🎮 Gaming
          </Button>
        </CardContent>

        <CardFooter>
          <Button className="w-full">Start Learning →</Button>
        </CardFooter>
      </Card>

      <p className="text-sm text-slate-400">
        Edit{" "}
        <code className="rounded bg-slate-100 px-1.5 py-0.5 font-mono text-slate-600">
          web/app/page.tsx
        </code>{" "}
        — saving reloads this page automatically.
      </p>
    </main>
  );
}
