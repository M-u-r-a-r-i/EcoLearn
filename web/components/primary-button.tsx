// A branded wrapper around the shadcn <Button>. It doesn't reinvent the button —
// it reuses shadcn's (which already inherits our indigo --primary) and just locks
// in EcoLearn's defaults: larger size, comfortable padding, soft shadow, and a
// subtle lift on hover. Use <PrimaryButton> for the main action on any screen so
// every primary CTA looks identical site-wide.

import * as React from "react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

type PrimaryButtonProps = React.ComponentProps<typeof Button>;

export function PrimaryButton({ className, size = "lg", ...props }: PrimaryButtonProps) {
  return (
    <Button
      size={size}
      className={cn(
        "h-12 rounded-xl px-8 text-base font-semibold shadow-soft transition-shadow hover:shadow-card-hover",
        className,
      )}
      {...props}
    />
  );
}
