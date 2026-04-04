"""
Lab 02: LLM JSON Output
Implements summarize_text(text) -> dict with keys:
  - title     : str   (short headline derived from the input)
  - points    : list  (exactly 3 key-point strings)
  - sentiment : str   ('positive' | 'neutral' | 'negative')
"""


def summarize_text(text: str) -> dict:
    """
    Return a structured JSON-style summary of the given text.

    Args:
        text: Any plain-text string to summarise.

    Returns:
        {
            "title":     <str>   – first 6 words of the text as a headline,
            "points":   [<str>, <str>, <str>]  – 3 key-point chunks,
            "sentiment": <str>  – 'positive', 'neutral', or 'negative'
        }

    Example:
        >>> summarize_text("AI is transforming urban mobility by optimizing traffic signals.")
        {
            'title': 'AI is transforming urban mobility by',
            'points': ['AI is transforming', 'urban mobility by', 'optimizing traffic signals.'],
            'sentiment': 'positive'
        }
    """
    words = text.split()

    # ── Title ────────────────────────────────────────────────────────────────
    title = " ".join(words[:6]) if len(words) >= 6 else " ".join(words)

    # ── 3 key points (split text into three roughly equal chunks) ────────────
    chunk = max(1, len(words) // 3)
    points = [
        " ".join(words[:chunk]),
        " ".join(words[chunk: chunk * 2]),
        " ".join(words[chunk * 2:]) or "Additional insights available",
    ]

    # ── Sentiment (keyword counting) ─────────────────────────────────────────
    POSITIVE = {
        "good", "great", "improving", "optimizing", "transforming",
        "better", "best", "efficient", "innovative", "advanced",
    }
    NEGATIVE = {
        "bad", "poor", "failing", "broken", "worst",
        "slow", "error", "problem", "issue", "dangerous",
    }

    lower = text.lower()
    pos = sum(1 for w in POSITIVE if w in lower)
    neg = sum(1 for w in NEGATIVE if w in lower)

    sentiment = "positive" if pos > neg else "negative" if neg > pos else "neutral"

    return {"title": title, "points": points, "sentiment": sentiment}
