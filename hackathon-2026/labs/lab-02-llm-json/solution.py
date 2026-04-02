"""
Lab 02: LLM JSON Output
Calls the Anthropic API and parses structured JSON output from the model.
"""
import json
import os
import requests


def summarize_text(text: str) -> dict:
    """
    Use an LLM to summarize text into structured JSON.

    Args:
        text: Any input string to summarize.

    Returns:
        A dict with keys:
            - 'title'     : str   — a short title for the text
            - 'points'    : list  — exactly 3 key bullet points
            - 'sentiment' : str   — one of 'positive', 'neutral', 'negative'
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")

    system_prompt = (
        "You are a structured data extractor. "
        "Return ONLY raw JSON with no markdown, no backticks, no explanation. "
        "The JSON must have exactly these keys: "
        "\"title\" (string), \"points\" (array of exactly 3 strings), "
        "\"sentiment\" (one of: positive, neutral, negative)."
    )

    user_prompt = f"Summarize the following text:\n\n{text}"

    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 512,
            "system": system_prompt,
            "messages": [
                {"role": "user", "content": user_prompt}
            ],
        },
    )

    raw = response.json()["content"][0]["text"].strip()

    # Strip markdown fences if model added them anyway
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    result = json.loads(raw)

    # Enforce exactly 3 points in case model returned more/less
    points = result.get("points", [])
    if len(points) > 3:
        points = points[:3]
    elif len(points) < 3:
        while len(points) < 3:
            points.append("N/A")
    result["points"] = points

    # Enforce valid sentiment
    if result.get("sentiment") not in {"positive", "neutral", "negative"}:
        result["sentiment"] = "neutral"

    return result
