from pprint import pprint
def summarize_text(text: str) -> dict:
    title = text[:30] + "..." if len(text) > 30 else text

    return {
        "title": title,
        "points": [
            "Main idea extracted",
            "Key detail identified",
            "Summary generated"
        ],
        "sentiment": "neutral"
    }
if __name__ == "__main__":
    sample_text = "AI is transforming urban mobility by optimizing traffic signals using computer vision."
    print("-"*100)
    result = summarize_text(sample_text)
    pprint(result)
    print("-"*100)
