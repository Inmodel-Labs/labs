def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using simple word overlap.

    Args:
        chunks:   List of text strings (the knowledge base).
        question: The user's question.

    Returns:
        The single chunk string with the highest word overlap score.
    """
    # TODO: Tokenize question (split on spaces, lowercase)
    question_words = question.lower().split()
    # TODO: For each chunk, count how many question words appear in it\
    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        chunk_words = chunk.lower().split()

        score = 0
        for word in question_words:
            if word in chunk_words:
                score += 1

        if score > best_score:
            best_score = score
            best_chunk = chunk
    # TODO: Return the chunk with the highest count
    return best_chunk if best_chunk else "No relevant context found."


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
    # TODO: Call retrieve() to get the best chunk
    context = retrieve(chunks, question)
    # TODO: Return {"context": <chunk>, "answer": <any non-empty string>}
    return {
        "context": context,
        "answer": f"Based on the context: {context}"
    }
