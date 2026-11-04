"""Parse a file once, then reuse the result until the file changes.

Why: the 30-student load test (scripts/load_test.py, 2026-10-02) found that a
single student's journey parsed YAML ~45 times — the diagnostic config, the
interest registry, the content scope and every lesson file's header, each
re-read on every call. With one Python process serving a whole class, that
CPU time queues up: p95 was 4.7 s.

The cache key is (resolved path, modification time, size), so editing a file —
a lesson, data/diagnostic.yaml — is picked up on the next call with no
restart, and a test pointing an env var at another file gets that file.

Callers must treat the returned object as READ-ONLY: it is shared between
requests. Copy it before changing anything.
"""

from __future__ import annotations

import threading
from pathlib import Path
from typing import Any, Callable

_MAX_ENTRIES = 4096  # a few thousand lesson files at most; then start over
_cache: dict[tuple[str, str], tuple[tuple[int, int], Any]] = {}
_lock = threading.Lock()


def cached_parse(path: str | Path, parse: Callable[[Path], Any], kind: str = "") -> Any:
    """`parse(path)`, reused while the file's mtime and size are unchanged.

    `kind` separates different parsers of the same file.
    """
    p = Path(path)  # not .resolve(): on Windows it costs a system call per lookup
    stat = p.stat()
    stamp = (stat.st_mtime_ns, stat.st_size)
    key = (kind, str(p))
    with _lock:
        hit = _cache.get(key)
    if hit is not None and hit[0] == stamp:
        return hit[1]
    value = parse(p)
    with _lock:
        if len(_cache) >= _MAX_ENTRIES:
            _cache.clear()
        _cache[key] = (stamp, value)
    return value


def clear() -> None:
    with _lock:
        _cache.clear()
