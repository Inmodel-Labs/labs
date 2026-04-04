"""
Lab 03: TOON Converter - Solution
"""


def json_to_toon(data: list[dict]) -> str:
    """
    Convert a list of uniform dicts to TOON format.

    Example output:
        # fields: id, name, score
        1 | Alice | 92
        2 | Bob | 87
    """
    if not data:
        return ""

    fields = list(data[0].keys())
    header = f"# fields: {', '.join(fields)}"

    rows = [
        " | ".join(str(row[field]) for field in fields)
        for row in data
    ]

    return "\n".join([header] + rows)


def count_tokens(text: str) -> int:
    """
    Simple token count proxy: split on whitespace and count words.
    Returns 0 for empty or whitespace-only strings.
    """
    return len(text.split()) if text.strip() else 0
