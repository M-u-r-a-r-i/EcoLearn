// Load data for a page and re-load when its inputs change.
//
// WHY: the obvious version — setLoading(true) at the top of an effect, then
// fetch — sets state synchronously inside the effect, which renders twice and
// is flagged by React's lint rules. Instead we remember WHICH request the
// current answer belongs to (`key`). If the key changed, the answer on screen is
// stale, so we are loading; no extra state or setState-in-effect needed. It also
// drops a slow answer for a chapter the student has already left.

"use client";

import { useEffect, useState } from "react";

import { friendlyMessage } from "@/lib/api";

type Settled<T> = { key: string; data: T; error: null } | { key: string; data: null; error: string };

export function useFetch<T>(key: string, fetcher: () => Promise<T>) {
  const [settled, setSettled] = useState<Settled<T> | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetcher().then(
      (data) => !cancelled && setSettled({ key, data, error: null }),
      (err) => !cancelled && setSettled({ key, data: null, error: friendlyMessage(err) }),
    );
    return () => {
      cancelled = true;
    };
    // `key` fully describes the request; the fetcher closure changes every render.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  const current = settled?.key === key ? settled : null;
  return { data: current?.data ?? null, error: current?.error ?? null, loading: current === null };
}
