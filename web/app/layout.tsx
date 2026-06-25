import type { Metadata } from "next";
import { Inter, Geist_Mono } from "next/font/google";
import "./globals.css";

import { SiteNav } from "@/components/site-nav";
import { StudentProvider } from "@/components/student-provider";

// next/font downloads & self-hosts the font at build time (fast, no layout shift)
// and exposes it as a CSS variable. We name it --font-sans so Tailwind's
// `font-sans` utility (applied to <html> in globals.css) uses Inter everywhere.
const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "EcoLearn — Learn through what you love",
  description:
    "EcoLearn personalises every lesson to a student's passions, turning the things they love into the way they learn.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
        <StudentProvider>
          <SiteNav />
          {children}
        </StudentProvider>
      </body>
    </html>
  );
}
