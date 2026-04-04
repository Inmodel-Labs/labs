"""
Lab 06: Healthcare Agents - Solution
"""

def is_anomaly(vitals: dict) -> bool:
    """
    Returns True if any vital sign is outside the normal range.

    Thresholds:
    - Heart Rate: [60, 100]       → anomaly if < 60 or > 100
    - BP Systolic: [90, 140]      → anomaly if < 90 or > 140
    - BP Diastolic: [60, 90]      → anomaly if < 60 or > 90
    - Oxygen Saturation: [95, 100] → anomaly if < 95
    """
    heart_rate       = vitals.get("heart_rate")
    bp_sys           = vitals.get("blood_pressure_sys")
    bp_dia           = vitals.get("blood_pressure_dia")
    oxygen           = vitals.get("oxygen_saturation")

    if heart_rate is not None and not (60 <= heart_rate <= 100):
        return True
    if bp_sys is not None and not (90 <= bp_sys <= 140):
        return True
    if bp_dia is not None and not (60 <= bp_dia <= 90):
        return True
    if oxygen is not None and oxygen < 95:
        return True

    return False


def recommend_intervention(vitals: dict, history: list = None) -> str:
    """
    Suggests an intervention based on the anomaly status.

    Returns:
    - "Immediate Physician Review" if any vital is anomalous.
    - "Continue Observation" if all vitals are within normal range.
    """
    if is_anomaly(vitals):
        return "Immediate Physician Review"
    return "Continue Observation"
