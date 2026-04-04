# ── Lab 03: TOON Converter ────────────────────────────────────────────────────

def json_to_toon(data: list[dict]) -> str:
    fields = list(data[0].keys())
    header = "# fields: " + ", ".join(fields)
    rows = [" | ".join(str(record[field]) for field in fields) for record in data]
    return "\n".join([header] + rows)


def count_tokens(text: str) -> int:
    return len(text.split())
