from typing import Optional
from collections import Counter


def count_by_class(detections: list[dict]) -> dict:
    """
    Count detections grouped by class name.

    Args:
        detections: List of detection dicts with 'class_name' key.

    Returns:
        A dict like {"car": 3, "truck": 1}
    """
    return dict(Counter(d["class_name"] for d in detections))


def filter_by_confidence(detections: list[dict], threshold: float) -> list[dict]:
    """
    Return only detections
