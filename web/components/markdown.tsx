// Renders markdown text that comes from the backend (lesson body, worked
// example, help answers).
//
// WHY a markdown renderer instead of just printing the string?
// The backend's text isn't plain text — its "polisher" emits MARKDOWN: **bold**,
// bullet lists, > blockquotes, paragraph breaks, and KaTeX math like $v = u + at$.
// If we dropped the raw string into a <div>, the browser would collapse the line
// breaks and show literal "**" and "$" characters. So we parse the markdown and
// turn it into real HTML elements:
//   • react-markdown  — markdown → React elements
//   • remark-gfm      — GitHub-flavoured extras (tables, lists, line breaks)
//   • remark-math + rehype-katex — turn $...$ / $$...$$ into rendered equations
// We never use dangerouslySetInnerHTML; react-markdown builds safe elements.

"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css"; // styles the rendered equations

import { cn } from "@/lib/utils";

export function Markdown({
  children,
  className,
}: {
  children: string;
  className?: string;
}) {
  return (
    // `prose` (Tailwind Typography) gives premium long-form defaults; the
    // prose-* overrides tune headings/links/strong to our brand + spacing.
    <div
      className={cn(
        "prose prose-slate max-w-none",
        "prose-headings:font-semibold prose-headings:text-foreground",
        "prose-p:leading-relaxed prose-p:text-foreground/90",
        "prose-strong:text-foreground prose-li:text-foreground/90",
        "prose-a:text-primary prose-a:no-underline hover:prose-a:underline",
        "prose-blockquote:border-l-primary prose-blockquote:text-muted-foreground",
        className,
      )}
    >
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeKatex]}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
