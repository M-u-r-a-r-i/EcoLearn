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

import { API_URL } from "@/lib/api";
import { cn } from "@/lib/utils";

// Lessons reference images by a path relative to the API's /media route
// (e.g. "figures/ohms_law/vi-ohmic-vs-lamp.svg"), so the same lesson file
// works wherever the API is hosted.
function mediaUrl(src: string | undefined): string | undefined {
  if (!src || /^(https?:)?\/\//.test(src) || src.startsWith("/")) return src;
  return `${API_URL}/media/${src}`;
}

// ![alt](src "caption") → the image with its caption underneath. Built from
// <span>s, not <figure>, because markdown wraps images in a <p> and a <figure>
// inside a <p> is invalid HTML. Figures sit on a white card so dark-text graphs
// stay readable in dark mode.
function LessonImage({ src, alt, title }: { src?: string | Blob; alt?: string; title?: string }) {
  return (
    <span className="my-6 block">
      {/* Plain <img>: images come from our own API, already size-checked by the validator. */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={mediaUrl(typeof src === "string" ? src : undefined)}
        alt={alt ?? ""}
        loading="lazy"
        className="mx-auto my-0 max-h-[28rem] w-auto rounded-xl border border-border bg-white shadow-soft"
      />
      {title && (
        <span className="mt-2 block text-center text-sm leading-snug text-muted-foreground">
          {title}
        </span>
      )}
    </span>
  );
}

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
        components={{ img: ({ src, alt, title }) => <LessonImage src={src} alt={alt} title={title} /> }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
