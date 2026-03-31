"""
Scenario: STEMI (ST-Elevation Myocardial Infarction)
A classic heart attack scenario for ER training.
"""

STEMI_SCENARIO = {
    "name": "STEMI — Inferior MI",
    "setting": "ER Triage Bay 3",
    "patient": {
        "name": "Mr. Arjun Rao",
        "age": 52,
        "gender": "Male",
        "complaint": "Severe chest pain radiating to the left arm, sweating, short of breath",
        "history": "Type 2 diabetic, smoker for 20 years, no prior cardiac events",
        "vitals": {
            "BP": "160/100 mmHg",
            "HR": "112 bpm",
            "SpO2": "94%",
            "RR": "22 breaths/min",
            "Temp": "37.1°C",
            "GCS": "15 (Alert)"
        }
    },
    "opening": (
        "You rush into Triage Bay 3. Mr. Arjun Rao, 52, is clutching his chest, "
        "pale and diaphoretic. He looks terrified. The nurse hands you his chart — "
        "onset 40 minutes ago. The clock is ticking."
    ),
    "interventions": {
        "ecg": {
            "keywords": ["ecg", "12-lead", "electrocardiogram", "ekg"],
            "score": 15,
            "feedback": "✅ ECG shows ST elevation in leads II, III, aVF → Inferior STEMI confirmed. Call the cath lab.",
            "updates_vitals": False,
        },
        "oxygen": {
            "keywords": ["oxygen", "o2", "mask", "spo2"],
            "score": 8,
            "feedback": "✅ Oxygen administered via non-rebreather mask. SpO2 climbing to 98%.",
            "updates_vitals": True,
            "new_vitals": {"SpO2": "98%"}
        },
        "aspirin": {
            "keywords": ["aspirin", "asa", "300mg", "antiplatelet"],
            "score": 20,
            "feedback": "✅ Aspirin 300mg given. Antiplatelet therapy initiated — critical step.",
            "updates_vitals": False,
        },
        "iv_access": {
            "keywords": ["iv", "intravenous", "cannula", "line", "access"],
            "score": 8,
            "feedback": "✅ Large-bore IV access established in the antecubital fossa.",
            "updates_vitals": False,
        },
        "troponin": {
            "keywords": ["troponin", "cardiac enzymes", "blood test", "biomarkers"],
            "score": 10,
            "feedback": "✅ Troponin I ordered. Results in 20 minutes — likely elevated.",
            "updates_vitals": False,
        },
        "morphine": {
            "keywords": ["morphine", "pain relief", "opioid", "analgesic"],
            "score": 5,
            "feedback": "⚠️  Morphine given. Pain easing but watch for hypotension — controversial in STEMI.",
            "updates_vitals": False,
        },
        "cath_lab": {
            "keywords": ["cath lab", "pci", "angioplasty", "catheterization", "activate"],
            "score": 25,
            "feedback": "✅ Cath lab activated! Door-to-balloon time initiated. This is the definitive treatment.",
            "updates_vitals": True,
            "new_vitals": {"HR": "98 bpm", "BP": "145/90 mmHg"}
        },
    },
    "danger_keywords": ["discharge", "send home", "wait", "not serious", "observe only"],
    "danger_penalty": 30,
    "max_turns": 10,
    "passing_score": 65,
}
