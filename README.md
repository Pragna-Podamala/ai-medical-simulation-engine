# 🏥 Medical Scenario Simulation Agent v2

An AI-powered medical training simulator for ER clinical decision-making. Practice high-pressure scenarios and get scored in real time.

**Powered by [Anthropic Claude](https://www.anthropic.com/) (claude-haiku-4-5)**

---

## Features

* 🤖 **Context-aware Claude agent** — responds dynamically to every clinical decision
* 🌿 **Branching scenario logic** — user actions directly influence patient trajectory and outcomes
* 📊 **Real-time state tracking** — vitals update after each intervention
* 🏆 **Outcome scoring system** — evaluates decisions and highlights missed steps
* 🏥 **3 scenarios** — STEMI, Sepsis, Anaphylaxis
* 🔌 **Multimodal-ready** — hooks for image synthesis and voice generation (plug in any API)
* ⚡ **Token-efficient design** — system prompt separation reduces per-turn token usage

---

## Project Structure

```
ai-medical-simulation-engine/
├── main.py                      # Entry point
├── agents/
│   └── simulation_engine.py     # Core agent: Claude API + state tracking + branching
├── scenarios/
│   ├── stemi.py                 # STEMI — Inferior MI
│   ├── sepsis.py                # Sepsis — Urosepsis
│   └── anaphylaxis.py           # Anaphylaxis — Severe allergic reaction
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
Choose a scenario → Enter clinical actions

YOU > order ecg
  [SIM] ECG shows ST elevation → Inferior STEMI confirmed

YOU > give aspirin
  [SIM] Aspirin given → Antiplatelet therapy initiated
```

Commands:

* `vitals`   → check current patient vitals
* `score`    → current score
* `history`  → all decisions made
* `quit`     → end + full performance report

---

## Architecture Notes

### Token Efficiency

The system prompt (scenario context, patient info, rules) is sent once as the `system` parameter instead of being injected into every user turn. This significantly reduces token usage.

### Multimodal Hooks

`simulation_engine.py` exposes `_generate_scene_image()` and `_generate_patient_voice()` — stub methods ready for integration with image (DALL·E, Stable Diffusion) and TTS APIs.

### Adding Scenarios

Create a new file in `scenarios/` following the schema in `stemi.py` and register it in `main.py`. No changes to the engine are required.

---

## Tech Stack

* Python 3.8+
* Anthropic Claude API (`claude-haiku-4-5`)
* Multi-turn conversation memory
* Modular simulation architecture

---

*Built as a prototype of an AI-powered medical simulation system exploring branching logic, context-aware agent behavior, and real-time state tracking.*
