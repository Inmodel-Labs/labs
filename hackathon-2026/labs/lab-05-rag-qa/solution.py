def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using simple word overlap.
    """
    question_words = set(question.lower().split())

    best_chunk = ""
    best_score = -1

    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for word in question_words if word in chunk_lower)
        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk if best_score > 0 else "No relevant context found."


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve the best context and build a simple answer.
    """
    context = retrieve(chunks, question)
    return {
        "context": context,
        "answer": context if context != "No relevant context found." else "I could not find an answer."
    }
