def json_to_toon(data: list[dict]) -> str:
    """
    Convert a list of uniform dicts to TOON format.

    Example:
        Input:  [{"id": 1, "name": "Alice", "score": 92}, ...]
        Output:
            # fields: id, name, score
            1 | Alice | 92
            2 | Bob | 87

    Returns:
        A single TOON-format string.
    """
    # Extract field names from the first dict
    fields = list(data[0].keys())

    # Build the header line: "# fields: key1, key2, ..."
    header = "# fields: " + ", ".join(fields)

    # Build each data row: "val1 | val2 | ..."
    rows = []
    for record in data:
        row = " | ".join(str(record[field]) for field in fields)
        rows.append(row)

    # Join header + all rows into a single string
    return "\n".join([header] + rows)


def count_tokens(text: str) -> int:
    """
    A simple proxy for token count: split on whitespace and count words.

    Args:
        text: Any string.

    Returns:
        Integer word count.
    """
    return len(text.split()) if text.strip() else 0
