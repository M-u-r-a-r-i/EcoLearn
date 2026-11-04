"""Usernames and starter passwords for accounts a teacher creates in bulk.

A teacher pastes a list of names; every student gets a username and a password
printed on a slip. Two constraints shape both:

  * **A 15-year-old has to type it, from paper, on a school computer.** So the
    username looks like the student's name ("aarav.k"), and the password is
    two short common words and two digits ("mango-river-42") — no 0/O or 1/l
    puzzles, no shift key.
  * **It must still be hard to guess.** Two words from a list of 256 and a
    number 10–99 give 256 × 256 × 90 ≈ 5.9 million combinations. bcrypt costs
    ~0.1 s per guess, so trying them all against one account takes about a week
    of non-stop requests — fine for a classroom pilot, and students can change it
    in Settings. (Rate-limiting the login endpoint is the next layer.)

`secrets`, not `random`: `random` is predictable from its earlier outputs, and
these are real credentials.
"""

from __future__ import annotations

import re
import secrets
import unicodedata
from typing import Callable

# Short, common, unambiguous, inoffensive words. Exactly 256.
_WORDS: tuple[str, ...] = (
    "apple", "arrow", "badge", "bagel", "bamboo", "banjo", "basil", "beach",
    "bean", "bear", "bell", "berry", "bike", "bird", "blaze", "bloom",
    "boat", "bolt", "book", "brave", "bread", "brick", "brook", "brush",
    "cabin", "cake", "camel", "candy", "canoe", "cargo", "cedar", "chalk",
    "charm", "chess", "chili", "cider", "cliff", "cloud", "clove", "coast",
    "cocoa", "comet", "coral", "corn", "crane", "creek", "crown", "cube",
    "daisy", "dance", "delta", "desk", "dingo", "disco", "dock", "dome",
    "dove", "drift", "drum", "dune", "eagle", "earth", "echo", "elbow",
    "elder", "ember", "fable", "fern", "field", "fig", "flame", "flute",
    "foam", "forest", "fox", "frost", "fudge", "gecko", "gem", "ginger",
    "glade", "globe", "glow", "goat", "grape", "grass", "gravy", "guava",
    "hammer", "harbor", "harp", "hazel", "hedge", "heron", "hill", "honey",
    "horse", "igloo", "india", "ink", "iris", "island", "ivory", "jade",
    "jam", "jazz", "jelly", "jet", "jolly", "judge", "juice", "jungle",
    "kayak", "kettle", "kite", "kiwi", "koala", "lake", "lamp", "lark",
    "lava", "lemon", "lily", "lime", "lion", "llama", "lotus", "lunar",
    "mango", "maple", "marble", "melon", "meteor", "mint", "moon", "moose",
    "moss", "mouse", "music", "nest", "noble", "noodle", "north", "nutmeg",
    "oak", "oasis", "ocean", "olive", "onion", "opal", "orbit", "otter",
    "owl", "paddle", "palm", "panda", "paper", "parrot", "peach", "pearl",
    "pebble", "pepper", "piano", "pine", "pixel", "planet", "plum", "pond",
    "poppy", "prism", "pump", "quail", "quartz", "quest", "quick", "quiet",
    "quilt", "radar", "radio", "rain", "raven", "reef", "ridge", "river",
    "robin", "rocket", "rose", "ruby", "sage", "salt", "sand", "saturn",
    "scarf", "seal", "shell", "silk", "sky", "sloth", "snow", "solar",
    "spark", "spice", "spoon", "star", "stone", "storm", "sugar", "sun",
    "swan", "table", "tango", "tea", "tiger", "toast", "topaz", "torch",
    "tower", "trail", "tulip", "tuna", "turtle", "umber", "unity", "valley",
    "vanilla", "velvet", "violet", "vivid", "wagon", "walnut", "water", "wave",
    "whale", "wheat", "willow", "wind", "wolf", "wonder", "yak", "yarn",
    "yellow", "yoga", "zebra", "zen", "zest", "zinc", "zipper", "zone",
    "acorn", "atlas", "breeze", "button", "candle", "cherry", "copper", "cricket",
)
assert len(_WORDS) == 256 and len(set(_WORDS)) == 256, "word list must be 256 unique words"

# Must agree with platform_api._USERNAME_PATTERN (3–20 chars, [a-z0-9_.],
# starting with a letter or digit).
_MAX_USERNAME = 20
_FALLBACK_STEM = "student"


def generate_password() -> str:
    """A fresh, typeable password like "mango-river-42" (always ≥ 8 characters)."""
    first = secrets.choice(_WORDS)
    second = secrets.choice(_WORDS)
    number = secrets.randbelow(90) + 10  # 10–99: always two digits
    return f"{first}-{second}-{number}"


def _ascii_words(name: str) -> list[str]:
    """Split a display name into lowercase ASCII words.

    NFKD separates letters from their accents ("José" → "Jose" + accent), so
    dropping the non-ASCII marks keeps the letter. Names with no Latin letters at
    all (e.g. written only in Devanagari) yield [], and get the fallback stem.
    """
    decomposed = unicodedata.normalize("NFKD", name)
    ascii_only = decomposed.encode("ascii", "ignore").decode("ascii").lower()
    return re.findall(r"[a-z0-9]+", ascii_only)


def username_stem(name: str) -> str:
    """The preferred username for a name: "Aarav Kumar" → "aarav.k".

    First name (up to 12 characters) plus the last name's initial; a single
    name stays as it is. Always a valid username on its own (≥ 3 characters,
    starts with a letter or digit), before any number is added to make it unique.
    """
    words = _ascii_words(name)
    if not words:
        return _FALLBACK_STEM
    stem = words[0][:12]
    if len(words) > 1:
        stem = f"{stem}.{words[-1][0]}"
    if len(stem) < 3:  # "Li" alone → "li.student" (the pattern needs 3+ characters)
        stem = f"{stem}.{_FALLBACK_STEM}"
    return stem


def unique_username(name: str, is_taken: Callable[[str], bool]) -> str:
    """The stem if it is free, else the stem plus the smallest free number ≥ 2.

    `is_taken` is asked about each candidate; the caller passes a function that
    checks both the database and the names already chosen in this roster.
    """
    stem = username_stem(name)
    if not is_taken(stem):
        return stem
    for n in range(2, 10_000):
        suffix = str(n)
        candidate = stem[: _MAX_USERNAME - len(suffix)] + suffix
        if not is_taken(candidate):
            return candidate
    # 10,000 students called "Aarav K" in one database is not a real situation;
    # fall back to randomness rather than loop forever.
    return f"{stem[:11]}{secrets.token_hex(4)}"
