"""
Lab 06: Healthcare Agents - Solution Template
"""

def is_anomaly(vitals: dict) -> bool:
    """
    Returns True if any vital sign is outside the normal range.
    
    Thresholds:
    - Heart Rate: [60, 100]
    - BP Systolic: [90, 140]
    - BP Diastolic: [60, 90]
    - Oxygen Saturation: [95, 100]
    """
    heart_rate = vitals["heart_rate"]
    sys = vitals["blood_pressure_sys"]
    dia = vitals["blood_pressure_dia"]
    oxygen = vitals["oxygen_saturation"]

    # TODO: Implement anomaly detection logic
    if heart_rate < 60 or heart_rate > 100:
        return True
    if sys < 90 or sys > 140:
        return True
    if dia < 60 or dia > 90:
        return True
    if oxygen < 95:
        return True
    
    return False

def recommend_intervention(vitals: dict, history: list = None) -> str:
    """
    Suggests an intervention based on the anomaly status.
    """
    if is_anomaly(vitals):
        return "Immediate Physician Review"
    return "Continue Observation"

# run python -m pytest to run this lab test in this labs-main\labs-main\hackathon-2026\labs\lab-06-healthcare-agents directory.
