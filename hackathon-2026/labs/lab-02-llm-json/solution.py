"""
Lab 02: LLM JSON Output - Solution
"""

import json
import re
import anthropic

client = anthropic.Anthropic()


def _extract_json(text: str) -> dict:
    """
    Robustly extract a JSON object from a string.
    Handles markdown fences and extra text around the JSON.
    """
    # Strip markdown code fences
    cleaned = re.sub(r"```(?:json)?|```", "", text).strip()

    # Try direct parse first
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Fallback: extract first {...} block in the text
    match = re.search(r"\{.*?\}", cleaned, re.DOTALL)
    if match:
        return json.loads(match.group())

    raise ValueError(f"No valid JSON found in model response:\n{text}")


def summarize_text(text: str) -> dict:
    """
    Use Claude to summarize a text into a structured JSON response.

    Returns:
        A dict with keys:
          - 'title'     (str)           : Short headline
          - 'points'    (list of 3 str) : Exactly 3 key takeaways
          - 'sentiment' (str)           : 'positive', 'neutral', or 'negative'
    """
    system_prompt = """
You are a JSON-only responder. Return ONLY raw JSON — no markdown, no backticks, no explanation.

Your response must strictly follow this schema:
{
  "title":     "<a short one-line headline summarizing the text>",
  "points":    ["<point 1>", "<point 2>", "<point 3>"],
  "sentiment": "<positive | neutral | negative>"
}

Rules:
- 'points' must contain EXACTLY 3 strings.
- 'sentiment' must be one of: positive, neutral, negative.
- Output nothing except the JSON object.
""".strip()

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system=system_prompt,
        messages=[
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ]
    )

    result = _extract_json(message.content[0].text)

    # --- Post-parse safety corrections ---

    # Ensure 'title' is a string
    if "title" not in result or not isinstance(result["title"], str):
        result["title"] = text[:60]

    # Ensure 'points' is a list of exactly 3 strings
    points = result.get("points", [])
    if not isinstance(points, list):
        points = [str(points)]
    while len(points) < 3:
        points.append("No additional point provided.")
    result["points"] = points[:3]

    # Ensure 'sentiment' is valid
    if result.get("sentiment") not in {"positive", "neutral", "negative"}:
        result["sentiment"] = "neutral"

    return result
