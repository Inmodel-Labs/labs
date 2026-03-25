# Lab 04: Vehicle Detection 🚗

**Points: 20 | Time: ~1-2 hours**

## Problem
Process a mock list of detection results (as if returned by a YOLO model) and extract useful statistics.

> **Note**: This lab does NOT require a GPU or camera. It simulates working with detection output data so you can practice the logic without any hardware dependency.

## Your Task
Implement the functions in `solution.py`.

## Detection Data Format
```python
# Each detection is a dict:
{"class_name": "car", "confidence": 0.91, "bbox": [100, 50, 200, 150]}
```

## Requirements
- `count_by_class(detections)` → returns a `dict` mapping class name to count
- `filter_by_confidence(detections, threshold)` → returns only detections above `threshold`
- `get_top_detection(detections)` → returns the single dict with the highest confidence
