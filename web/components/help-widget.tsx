// "Stuck? Ask for help" widget, embedded in the lesson page.
//
// It calls the LIVE pipeline (POST /api/help), which is slow (a few seconds),
// so it keeps its own little conversation and shows a "thinking" state while the
// request is in flight. The student can ask follow-ups without leaving the page.

"use client";

import { useEffect, useRef, useState } from "react";
import { Sparkles, SendHorizontal } from "lucide-react";

import { askHelp } from "@/lib/api";
import { Markdown } from "@/components/markdown";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";

interface Message {
  role: "user" | "assistant";
  text: string;
}

export function HelpWidget({
  studentId,
  conceptId,
}: {
  studentId: string;
  conceptId: string;
}) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // Auto-scroll the conversation to the newest message.
  const bottomRef = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function handleSend(e: React.FormEvent) {
    e.preventDefault(); // don't reload the page on form submit
    const question = input.trim();
    if (!question || loading) return;

    // Optimistically show the student's question, clear the box.
    setMessages((prev) => [...prev, { role: "user", text: question }]);
    setInput("");
    setLoading(true);

    try {
      const res = await askHelp(studentId, conceptId, question);
      setMessages((prev) => [...prev, { role: "assistant", text: res.answer }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "_Sorry, I couldn't reach the tutor just now. Please make sure the backend is running and try again._",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  const hasConversation = messages.length > 0 || loading;

  return (
    <Card className="border-primary/20 bg-card shadow-card">
      <CardHeader>
        <CardTitle className="flex items-center gap-2 text-base text-foreground">
          <span className="flex size-7 items-center justify-center rounded-full bg-primary/10">
            <Sparkles className="size-4 text-primary" />
          </span>
          Stuck? Ask for help
        </CardTitle>
      </CardHeader>

      <CardContent className="flex flex-col gap-4">
        {/* Friendly empty state */}
        {!hasConversation && (
          <p className="text-sm text-muted-foreground">
            Ask anything about this concept — I&apos;ll explain it another way,
            grounded in your interest. You can keep asking follow-ups right here.
          </p>
        )}

        {/* Conversation */}
        {hasConversation && (
          <div className="flex max-h-96 flex-col gap-3 overflow-y-auto pr-1">
            {messages.map((m, i) =>
              m.role === "user" ? (
                <div
                  key={i}
                  className="max-w-[85%] self-end rounded-2xl rounded-br-sm bg-primary px-4 py-2 text-sm text-primary-foreground"
                >
                  {m.text}
                </div>
              ) : (
                <div
                  key={i}
                  className="max-w-[90%] self-start rounded-2xl rounded-bl-sm border border-border bg-muted/40 px-4 py-3"
                >
                  <Markdown className="prose-sm">{m.text}</Markdown>
                </div>
              ),
            )}

            {/* Thinking state — live call takes a few seconds */}
            {loading && (
              <div className="flex max-w-[90%] items-center gap-2 self-start rounded-2xl rounded-bl-sm border border-border bg-muted/40 px-4 py-3 text-sm text-muted-foreground">
                <Sparkles className="size-4 animate-pulse text-primary" />
                <span>Thinking</span>
                <span className="inline-flex gap-0.5">
                  <Dot delay="0ms" />
                  <Dot delay="150ms" />
                  <Dot delay="300ms" />
                </span>
              </div>
            )}

            <div ref={bottomRef} />
          </div>
        )}

        {/* Composer */}
        <form onSubmit={handleSend} className="flex items-center gap-2">
          <Input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="e.g. Why is displacement a vector but distance isn't?"
            disabled={loading}
            aria-label="Ask a question"
          />
          <Button
            type="submit"
            size="icon"
            disabled={loading || !input.trim()}
            aria-label="Send"
          >
            <SendHorizontal className="size-4" />
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}

// One bouncing dot for the "thinking…" indicator.
function Dot({ delay }: { delay: string }) {
  return (
    <span
      className="size-1.5 animate-bounce rounded-full bg-muted-foreground"
      style={{ animationDelay: delay }}
    />
  );
}
