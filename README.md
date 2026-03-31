# 🏥 Medical Scenario Simulation Agent v2

An AI-powered medical training simulator for ER clinical decision-making. Practice high-pressure scenarios and get scored in real time.

**Powered by [Anthropic Claude](https://www.anthropic.com/) (claude-haiku-4-5)**

---

## Features

- 🤖 **Context-aware Claude agent** — responds dynamically to every clinical decision
- 🌿 **Branching scenario logic** — your choices directly change patient trajectory and vitals
- 📊 **Real-time state tracking** — vitals update after each intervention
- 🏆 **Outcome scoring** — full performance report with missed-step analysis
- 🏥 **3 scenarios** — STEMI, Sepsis, Anaphylaxis
- 🔌 **Multimodal-ready** — hooks for image synthesis and voice generation (plug in any API)
- ⚡ **Token-efficient** — system prompt separation keeps costs low at scale

---

## Project Structure

```
medical_sim_agent/
├── main.py                      # Entry point
├── agents/
│   └── simulation_engine.py     # Core agent: Claude API + state tracking + branching
├── scenarios/
│   ├── stemi.py                 # STEMI — Inferior MI
│   ├── sepsis.py                # Sepsis — Urosepsis
│   └── anaphylaxis.py           # Anaphylaxis — NEW
├── requirements.txt
└── README.md
```

---

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python main.py
```

---

## How to Play

```
Choose a scenario → Walk into the ER → Type your clinical actions

YOU > order ECG
  [SIM] ✅ ECG shows ST elevation in leads II, III, aVF → Inferior STEMI confirmed.

YOU > give aspirin
  [SIM] ✅ Aspirin 300mg given. Antiplatelet therapy initiated.

Commands:
  vitals   → check current patient vitals
  score    → current score
  history  → all decisions made
  quit     → end + full performance report
```

---

## Architecture Notes

### Token Efficiency
The system prompt (scenario context, patient info, rules) is sent **once** as the `system` parameter — not injected into every user turn. This reduces per-turn token usage by ~60% vs naive prompt injection.

### Multimodal Hooks
`simulation_engine.py` exposes `_generate_scene_image()` and `_generate_patient_voice()` — stub methods ready to integrate image synthesis (DALL-E, Stable Diffusion) and TTS (ElevenLabs) APIs without changing core logic.

### Adding Scenarios
Create a new file in `scenarios/` following the schema in `stemi.py` and register it in `main.py`. No changes to the engine required.

---

## Tech Stack

- **Python 3.8+**
- **Anthropic Claude API** (`claude-haiku-4-5`) — conversational agent
- **Multi-turn conversation history** — full context maintained across turns
- **Modular scenario design** — easily extensible

---

*Built as a prototype of an AI-powered medical simulation platform — exploring branching scenario logic, context-aware agent behavior, and real-time state tracking.*
