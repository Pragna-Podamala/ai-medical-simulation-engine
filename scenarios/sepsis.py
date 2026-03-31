"""
Scenario: Sepsis — Infection-Induced Shock
A sepsis recognition and management scenario.
"""

SEPSIS_SCENARIO = {
    "name": "Sepsis — Suspected Urosepsis",
    "setting": "ER Bay 5",
    "patient": {
        "name": "Mrs. Kavitha Nair",
        "age": 68,
        "gender": "Female",
        "complaint": "Fever, confusion, decreased urine output, flank pain for 2 days",
        "history": "Hypertension, recurrent UTIs, lives alone",
        "vitals": {
            "BP": "88/60 mmHg",
            "HR": "124 bpm",
            "SpO2": "92%",
            "RR": "26 breaths/min",
            "Temp": "39.4°C",
            "GCS": "13 (Confused)"
        }
    },
    "opening": (
        "Mrs. Kavitha Nair, 68, is brought in by her neighbor. She's confused, "
        "flushed, and barely responsive to questions. Her BP is critically low. "
        "The nurse flags this as a potential sepsis alert. You have minutes."
    ),
    "interventions": {
        "blood_cultures": {
            "keywords": ["blood culture", "cultures", "culture"],
            "score": 15,
            "feedback": "✅ Blood cultures drawn x2 from separate sites. Critical before antibiotics.",
            "updates_vitals": False,
        },
        "iv_fluids": {
            "keywords": ["fluids", "saline", "iv fluid", "bolus", "resuscitation", "500ml", "1 litre"],
            "score": 20,
            "feedback": "✅ 30ml/kg IV fluid bolus started. BP beginning to respond.",
            "updates_vitals": True,
            "new_vitals": {"BP": "100/70 mmHg"}
        },
        "antibiotics": {
            "keywords": ["antibiotic", "piperacillin", "tazobactam", "ceftriaxone", "meropenem"],
            "score": 25,
            "feedback": "✅ Broad-spectrum antibiotics given. Every hour of delay increases mortality by 7%.",
            "updates_vitals": True,
            "new_vitals": {"Temp": "38.8°C"}
        },
        "oxygen": {
            "keywords": ["oxygen", "o2", "mask", "spo2"],
            "score": 8,
            "feedback": "✅ Oxygen via face mask. SpO2 improving to 96%.",
            "updates_vitals": True,
            "new_vitals": {"SpO2": "96%"}
        },
        "urine_output": {
            "keywords": ["catheter", "urine", "foley", "output", "urine output"],
            "score": 10,
            "feedback": "✅ Foley catheter inserted. Urine output monitoring started — dark concentrated urine noted.",
            "updates_vitals": False,
        },
        "lactate": {
            "keywords": ["lactate", "lactic acid", "abg", "arterial blood gas"],
            "score": 12,
            "feedback": "✅ Lactate: 4.2 mmol/L — confirms septic shock. Escalate care.",
            "updates_vitals": False,
        },
        "icu": {
            "keywords": ["icu", "intensive care", "critical care", "transfer", "escalate"],
            "score": 20,
            "feedback": "✅ ICU team activated. Patient being transferred for vasopressors and monitoring.",
            "updates_vitals": True,
            "new_vitals": {"BP": "108/72 mmHg", "HR": "108 bpm"}
        },
    },
    "danger_keywords": ["discharge", "send home", "wait", "oral antibiotics", "not serious"],
    "danger_penalty": 30,
    "max_turns": 10,
    "passing_score": 65,
}
