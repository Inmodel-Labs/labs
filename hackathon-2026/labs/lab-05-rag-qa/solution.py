import re
from collections import Counter

# Common stopwords to ignore during matching
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "what", "how",
    "when", "where", "who", "which", "does", "do", "did", "for",
    "in", "on", "at", "to", "of", "and", "or", "it", "this", "that"
}

def tokenize(text: str) -> list[str]:
    """Lowercase, remove punctuation, split into meaningful words."""
    return [
        word for word in re.findall(r'\b[a-z]+\b', text.lower())
        if word not in STOPWORDS
    ]

def score_chunk(chunk: str, question_tokens: list[str]) -> float:
    """
    Score a chunk based on weighted keyword overlap.
    - Rewards chunks that match more unique question keywords.
    - Uses term frequency in chunk to boost confident matches.
    """
    if not question_tokens:
        return 0.0

    chunk_tokens = tokenize(chunk)
    chunk_freq = Counter(chunk_tokens)
    question_set = set(question_tokens)

    score = 0.0
    for word in question_set:
        if word in chunk_freq:
            # Boost s
