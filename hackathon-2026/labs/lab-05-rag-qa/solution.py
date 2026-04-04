"""
Lab 05: RAG Q&A - Solution
"""

import re
from collections import Counter

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "what", "how",
    "when", "where", "who", "which", "does", "do", "did", "for",
    "in", "on", "at", "to", "of", "and", "or", "it", "this", "that"
}


def tokenize(text: str) -> list[str]:
    """Lowercase, remove punctuation, filter stopwords."""
    return [
        word for word in re.findall(r'\b[a-z]+\b', text.lower())
        if word not in STOPWORDS
    ]


def score_chunk(chunk: str, question_tokens: list[str]) -> float:
    """
    Score a chunk using weighted keyword overlap + term frequency boost.
    Normalized by number of question keywords.
    """
    if not question_tokens:
        return 0.0

    chunk_tokens = tokenize(chunk)
    chunk_freq   = Counter(chunk_tokens)
    question_set = set(question_tokens)

    score = sum(
        1 + (0.1 * chunk_freq[word])
        for word in question_set
        if word in chunk_freq
    )
    return score / len(question_set)


def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using weighted keyword overlap.
    """
    if not chunks or not question.strip():
        return "No relevant context found."

    question_tokens = tokenize(question)
    if not question_tokens:
        return "No relevant context found."

    scored = [(chunk, score_chunk(chunk, question_tokens)) for chunk in chunks]
    best_chunk, best_score = max(scored, key=lambda x: x[1])

    return best_chunk if best_score > 0 else "No relevant context found."


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve best context and generate a structured answer.
    """
    context = retrieve(chunks, question)

    if context == "No relevant context found.":
        return {
            "context": context,
            "answer": "I could not find relevant information to answer your question."
        }

    return {
        "context": context,
        "answer": f"Based on the available information: {context}"
    }
