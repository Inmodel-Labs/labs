"""
Lab 05: RAG Q&A
Implements the retrieval core of a Retrieval-Augmented Generation pipeline.

Functions:
    retrieve(chunks, question) -> str   – returns the single best-matching chunk
    answer(chunks, question)   -> dict  – returns {'context': str, 'answer': str}
"""


def retrieve(chunks: list[str], question: str) -> str:
    """
    Find the most relevant chunk using word-overlap scoring.

    Strategy:
      - Tokenise the question into a set of lowercase words.
      - Score each chunk by counting how many question words appear in it.
      - Return the chunk with the highest score (first chunk wins on tie).

    Args:
        chunks:   Non-empty list of text strings (the knowledge base).
        question: The user's natural-language question.

    Returns:
        The single chunk string with the highest word-overlap score.

    Example:
        >>> retrieve(["YOLO detects objects.", "RAG reduces hallucinations."],
        ...          "What is YOLO?")
        'YOLO detects objects.'
    """
    question_words = set(question.lower().split())

    best_chunk = chunks[0]
    best_score = -1

    for chunk in chunks:
        chunk_lower = chunk.lower()
        # Count how many distinct question words appear anywhere in this chunk
        score = sum(1 for word in question_words if word in chunk_lower)
        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve the best context chunk and generate a grounded answer.

    Args:
        chunks:   The knowledge base (list of text strings).
        question: The user's question.

    Returns:
        A dict with:
            'context' (str) – the retrieved chunk used as evidence
            'answer'  (str) – a non-empty answer grounded in that context

    Example:
        >>> answer(["RAG reduces hallucinations."], "What is RAG?")
        {
            'context': 'RAG reduces hallucinations.',
            'answer':  'Based on the context: RAG reduces hallucinations.'
        }
    """
    context = retrieve(chunks, question)
    return {
        "context": context,
        "answer": f"Based on the context: {context}",
    }
