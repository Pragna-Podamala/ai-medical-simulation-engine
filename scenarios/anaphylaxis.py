"""
Scenario: Anaphylaxis — Severe Allergic Reaction
Time-critical scenario testing airway + epinephrine priority.
"""

ANAPHYLAXIS_SCENARIO = {
    "name": "Anaphylaxis — Severe Allergic Reaction",
    "setting": "ER Walk-In, Triage Bay 1",
    "patient": {
        "name": "Rohan Mehta",
        "age": 24,
        "gender": "Male",
        "complaint": "Throat swelling, hives, difficulty breathing after eating at a restaurant",
        "history": "Known peanut allergy, forgot his EpiPen today",
        "vitals": {
            "BP": "82/50 mmHg",
            "HR": "138 bpm",
            "SpO2": "89%",
            "RR": "30 breaths/min",
            "Temp": "37.2°C",
            "GCS": "14 (Drowsy)"
        }
    },
    "opening": (
        "Rohan Mehta, 24, staggers through the ER doors supported by a friend. "
        "His face is flushed and swollen, lips turning blue. He's gasping — "
        "'I... can't breathe.' Stridor is audible from across the room. You have seconds."
    ),
    "interventions": {
        "epinephrine": {
            "keywords": ["epinephrine", "epipen", "adrenaline", "0.3mg", "im", "intramuscular"],
            "score": 30,
            "feedback": "✅ Epinephrine 0.3mg IM given to lateral thigh. This is the FIRST-LINE treatment — no delays.",
            "updates_vitals": True,
            "new_vitals": {"BP": "100/65 mmHg", "HR": "118 bpm", "SpO2": "93%"},
            "rationale": "Epinephrine IM is the only first-line drug for anaphylaxis — must be given immediately."
        },
        "airway": {
            "keywords": ["airway", "oxygen", "o2", "intubate", "mask", "bvm", "non-rebreather"],
            "score": 20,
            "feedback": "✅ High-flow O2 via non-rebreather mask. SpO2 climbing — airway still patent for now.",
            "updates_vitals": True,
            "new_vitals": {"SpO2": "95%"},
            "rationale": "Airway management is critical — anaphylaxis can cause complete obstruction within minutes."
        },
        "iv_access": {
            "keywords": ["iv", "intravenous", "cannula", "line", "access"],
            "score": 10,
            "feedback": "✅ Large-bore IV established. Ready for fluid resuscitation.",
            "updates_vitals": False,
            "rationale": "IV access needed for fluids and second-line medications."
        },
        "iv_fluids": {
            "keywords": ["fluids", "saline", "bolus", "resuscitation", "iv fluid"],
            "score": 15,
            "feedback": "✅ 1L normal saline bolus running. BP responding — distributive shock being corrected.",
            "updates_vitals": True,
            "new_vitals": {"BP": "108/72 mmHg"},
            "rationale": "IV fluids correct distributive shock from massive vasodilation."
        },
        "antihistamine": {
            "keywords": ["antihistamine", "benadryl", "diphenhydramine", "chlorphenamine", "cetirizine"],
            "score": 8,
            "feedback": "⚠️  Antihistamine given. Helpful for hives — but NOT a substitute for epinephrine in anaphylaxis.",
            "updates_vitals": False,
            "rationale": "Antihistamines are second-line — never replace epinephrine as the primary treatment."
        },
        "steroids": {
            "keywords": ["steroid", "hydrocortisone", "methylprednisolone", "dexamethasone", "prednisolone"],
            "score": 8,
            "feedback": "✅ IV hydrocortisone given. Helps prevent biphasic reaction — good second-line move.",
            "updates_vitals": False,
            "rationale": "Steroids prevent biphasic reactions, which can occur hours after initial anaphylaxis."
        },
        "observe_monitor": {
            "keywords": ["observe", "monitor", "admit", "watch", "keep", "ecg", "telemetry"],
            "score": 9,
            "feedback": "✅ Patient placed on continuous monitoring. Biphasic anaphylaxis can occur 1-72 hours later.",
            "updates_vitals": False,
            "rationale": "Minimum 4-6 hours observation mandatory after anaphylaxis due to biphasic risk."
        },
    },
    "danger_keywords": ["discharge", "send home", "oral", "wait", "antihistamine only", "not serious"],
    "danger_penalty": 30,
    "max_turns": 10,
    "passing_score": 65,
}
