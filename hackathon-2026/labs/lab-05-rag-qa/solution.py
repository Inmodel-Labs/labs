def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using simple word overlap.

    Args:
        chunks:   List of text strings (the knowledge base).
        question: The user's question.

    Returns:
        The single chunk string with the highest word overlap score.
    """
    # Tokenize question: split on spaces, lowercase
    question_words = set(question.lower().split())

    # For each chunk, count how many question words appear in it
    best_chunk = max(chunks, key=lambda chunk: len(
        question_words & set(chunk.lower().split())
    ))

    return best_chunk


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve the best context and build a simple answer.

    Args:
        chunks:   The knowledge base.
        question: The user's question.

    Returns:
        A dict with keys: 'context' (str) and 'answer' (str).
        'answer' must be a non-empty string.
    """
    # Call retrieve() to get the best chunk
    context = retrieve(chunks, question)

    # Return context and a non-empty answer string
    return {
        "context": context,
        "answer": context
    }
