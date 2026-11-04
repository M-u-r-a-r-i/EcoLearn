import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";

export const metadata: Metadata = {
  title: "EcoLearn — Physics that clicks",
  description: "A personal physics tutor that connects Class 11–12 concepts to the things you love.",
  icons: { icon: "/favicon.svg", apple: "/favicon.svg" },
};

export default function RootLayout({ children }: Readonly<{ children: ReactNode }>) {
  return <html lang="en" className="dark" suppressHydrationWarning><body>{children}</body></html>;
}