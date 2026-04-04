def json_to_toon(data: list[dict]) -> str:
    """
    Convert a list of uniform dicts to TOON format.

    Example:
        Input:  [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        Output:
            # fields: id, name
            1 | Alice
            2 | Bob

    Returns:
        A single TOON-format string.
    """
    if not data:
        return ""
    # TODO: Extract the field names from the first dict
    fields = list(data[0].keys())

    # TODO: Build the header line: "# fields: key1, key2, ..."
    header = "# fields: " + ", ".join(fields)

    # TODO: Build each data row: "val1 | val2 | ..."
    rows = []
    for item in data:
        row = " | ".join(str(item[field]) for field in fields)
        rows.append(row)

    # TODO: Join and return all lines as a string
    return "\n".join([header] + rows)
    


def count_tokens(text: str) -> int:
    """
    A simple proxy for token count: split on whitespace and count words.
    
    Args:
        text: Any string.

    Returns:
        Integer word count.
    """
    # TODO: Implement this
    if not text.strip():    #returning the number of words or tokens.
        return 0
    return len(text.split())

if __name__ == "__main__":
    data = [
        {"id": 1, "name": "Alice", "score": 92},
        {"id": 2, "name": "Bob", "score": 87},
    ]

    result = json_to_toon(data)
    print(result)
