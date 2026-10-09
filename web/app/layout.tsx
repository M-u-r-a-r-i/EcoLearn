import type { Metadata } from "next";
import { Geist_Mono } from "next/font/google";
import "./globals.css";

import { SiteNav } from "@/components/site-nav";
import { AuthProvider } from "@/components/auth-provider";
import { THEME_BOOT_SCRIPT } from "@/components/theme-toggle";
import { Toaster } from "@/components/toast";

// Body and display fonts are the house system stacks (--font-body / --font-display in
// globals.css); only the monospace face is downloaded.
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
      className={`${geistMono.variable} h-full antialiased`}
      // The theme script below may add class="dark" before React hydrates.
      suppressHydrationWarning
    >
      <head>
        {/* Applies the saved light/dark choice before the first paint (no flash). */}
        <script dangerouslySetInnerHTML={{ __html: THEME_BOOT_SCRIPT }} />
      </head>
      <body className="min-h-full flex flex-col pb-16 md:pb-0 print:pb-0">
        <AuthProvider>
          <Toaster>
            <SiteNav />
            {children}
          </Toaster>
        </AuthProvider>
      </body>
    </html>
  );
}
