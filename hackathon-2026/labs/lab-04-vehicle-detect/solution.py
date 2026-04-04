# ── Lab 04: Vehicle Detection ─────────────────────────────────────────────────

from typing import Optional


def detect_vehicles(detections: list[dict]) -> int:
    VEHICLE_CLASSES = {"car", "truck", "bus", "motorcycle"}
    return sum(
        1 for d in detections
        if d["class"] in VEHICLE_CLASSES and d["conf"] > 0.5
    )


def count_by_class(detections):
    counts = {}
    for d in detections:
        cls = d["class_name"]
        counts[cls] = counts.get(cls, 0) + 1
    return counts


def filter_by_confidence(detections, threshold):
    return [d for d in detections if d["confidence"] > threshold]


def get_top_detection(detections) -> Optional[dict]:
    return max(detections, key=lambda d: d["confidence"]) if detections else None
