"""
Lab 06: Healthcare Agents
Monitors patient vitals and flags anomalies requiring physician intervention.
"""

# ── Thresholds ────────────────────────────────────────────────────────────────
THRESHOLDS = {
    "heart_rate":         {"min": 60,  "max": 100},
    "blood_pressure_sys": {"min": 90,  "max": 140},
    "blood_pressure_dia": {"min": 60,  "max": 90},
    "oxygen_saturation":  {"min": 95,  "max": float("inf")},  # no upper bound
}


def is_anomaly(vitals: dict) -> bool:
    """
    Returns True if ANY vital sign falls outside its normal range.

    Args:
        vitals (dict): {
            "heart_rate": int,
            "blood_pressure_sys": int,
            "blood_pressure_dia": int,
            "oxygen_saturation": int | float
        }

    Returns:
        bool: True = anomaly detected, False = all vitals normal.
    """
    checks = {
        "heart_rate":         vitals.get("heart_rate"),
        "blood_pressure_sys": vitals.get("blood_pressure_sys"),
        "blood_pressure_dia": vitals.get("blood_pressure_dia"),
        "oxygen_saturation":  vitals.get("oxygen_saturation"),
    }

    for key, value in checks.items():
        if value is None:
            continue                          # skip missing readings
        limits = THRESHOLDS[key]
        if value < limits["min"] or value > limits["max"]:
            return True

    return False


def recommend_intervention(vitals: dict, history: list = None) -> str:
    """
    Suggests a clinical action based on the patient's current vitals
    and (optionally) their recent history.

    Args:
        vitals  (dict): Current vital signs (same structure as above).
        history (list): Optional list of previous vitals dicts.

    Returns:
        str: A recommendation string.
    """
    if history is None:
        history = []

    anomaly_now = is_anomaly(vitals)

    # Count how many recent readings were also anomalies (trend detection)
    recent_anomalies = sum(1 for v in history if is_anomaly(v))

    if anomaly_now:
        # Build a human-readable list of the offending vitals
        flags = _flag_details(vitals)
        base = "Immediate Physician Review"
        if recent_anomalies > 0:
            return (
                f"{base} — persistent anomaly detected across "
                f"{recent_anomalies + 1} reading(s). Affected: {flags}."
            )
        return f"{base} — anomaly detected. Affected: {flags}."

    if recent_anomalies > 0:
        return (
            "Continue Observation — current vitals normal, but "
            f"{recent_anomalies} recent anomalous reading(s) noted. Monitor closely."
        )

    return "Continue Observation — all vitals within normal range."


# ── Helper ────────────────────────────────────────────────────────────────────

def _flag_details(vitals: dict) -> str:
    """Returns a readable string listing each out-of-range vital and its value."""
    labels = {
        "heart_rate":         "Heart Rate",
        "blood_pressure_sys": "BP Systolic",
        "blood_pressure_dia": "BP Diastolic",
        "oxygen_saturation":  "Oxygen Saturation",
    }
    flagged = []
    for key, label in labels.items():
        value = vitals.get(key)
        if value is None:
            continue
        limits = THRESHOLDS[key]
        if value < limits["min"] or value > limits["max"]:
            flagged.append(f"{label}={value}")
    return ", ".join(flagged) if flagged else "unknown"


# ── Quick demo ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    normal = {
        "heart_rate": 85,
        "blood_pressure_sys": 120,
        "blood_pressure_dia": 80,
        "oxygen_saturation": 98,
    }

    critical = {
        "heart_rate": 130,
        "blood_pressure_sys": 160,
        "blood_pressure_dia": 95,
        "oxygen_saturation": 92,
    }

    borderline = {
        "heart_rate": 72,
        "blood_pressure_sys": 118,
        "blood_pressure_dia": 78,
        "oxygen_saturation": 94,   # just below threshold
    }

    for label, v in [("Normal", normal), ("Critical", critical), ("Borderline", borderline)]:
        anomaly = is_anomaly(v)
        recommendation = recommend_intervention(v, history=[critical])
        print(f"\n[{label}]")
        print(f"  Anomaly?       {anomaly}")
        print(f"  Recommendation: {recommendation}")
