"""
Lab 04: Vehicle Detection - Solution
"""

from typing import Optional
from collections import Counter


def count_by_class(detections: list[dict]) -> dict:
    """
    Count detections grouped by class name.

    Returns:
        A dict like {"car": 3, "truck": 1}
    """
    return dict(Counter(d["class_name"] for d in detections))


def filter_by_confidence(detections: list[dict], threshold: float) -> list[dict]:
    """
    Return only detections where confidence > threshold (exclusive),
    sorted by confidence descending.
    """
    return sorted(
        [d for d in detections if d["confidence"] > threshold],
        key=lambda d: d["confidence"],
        reverse=True
    )


def get_top_detection(detections: list[dict]) -> Optional[dict]:
    """
    Return the detection with the highest confidence score.
    Returns None if list is empty.
    """
    if not detections:
        return None
    return max(detections, key=lambda d: d["confidence"])
