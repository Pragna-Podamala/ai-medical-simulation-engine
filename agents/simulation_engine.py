"""
Simulation Engine v2
--------------------
Upgraded core agent:
- Powered by Anthropic Claude (claude-haiku-4-5) instead of Gemini
- Token-efficient prompt design (system prompt separation)
- Multimodal-ready architecture (image/audio hooks)
- Richer narrative continuity tracking
- Structured scoring with decision quality analysis

Author: Podamala Pragna
"""

import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env


class SimulationEngine:
    def __init__(self, scenario: dict):
        self.scenario = scenario
        self.patient = scenario["patient"]
        self.vitals = dict(scenario["patient"]["vitals"])
        self.interventions = scenario["interventions"]
        self.completed = set()
        self.decisions = []
        self.score = 100
        self.turn = 0
        self.conversation_history = []   # full multi-turn history for Claude

    # ── SYSTEM PROMPT (sent once, not repeated every turn — token efficient) ─
    def _system_prompt(self) -> str:
        return f"""You are a high-fidelity medical simulation engine for ER training.

SCENARIO : {self.scenario['name']}
SETTING  : {self.scenario['setting']}
PATIENT  : {self.patient['name']}, {self.patient['age']}{self.patient['gender'][0]} — {self.patient['complaint']}
HISTORY  : {self.patient['history']}

RULES:
- If the trainee speaks TO the patient → respond AS the patient (scared, first-person, 1-2 lines).
- If the trainee performs a clinical action → respond as a clinical narrator (3-4 lines, medically accurate).
- Never give away the next step directly — hint through monitor changes or patient behavior.
- Be terse, realistic, and clinically accurate.
- Keep every reply under 4 sentences."""

    # ── USER TURN PROMPT (minimal — just state delta + action) ───────────────
    def _user_prompt(self, user_input: str) -> str:
        vitals_str = " | ".join(f"{k}: {v}" for k, v in self.vitals.items())
        done_str = ", ".join(self.completed) if self.completed else "none"
        return f"""[Turn {self.turn} | Score: {self.score}/100 | Done: {done_str}]
[Vitals: {vitals_str}]

TRAINEE: {user_input}"""

    # ── BRANCHING LOGIC ───────────────────────────────────────────────────────
    def _check_interventions(self, user_input: str):
        ui = user_input.lower()
        for key, data in self.interventions.items():
            if key in self.completed:
                continue
            if any(kw in ui for kw in data["keywords"]):
                self.completed.add(key)
                self.score = min(100, self.score + data["score"])
                print(f"\n  [SIM] {data['feedback']}\n")
                if data.get("updates_vitals") and "new_vitals" in data:
                    self.vitals.update(data["new_vitals"])
                return

        if any(kw in ui for kw in self.scenario["danger_keywords"]):
            self.score = max(0, self.score - self.scenario["danger_penalty"])
            print(f"\n  [SIM] ❌ DANGEROUS DECISION — score -{self.scenario['danger_penalty']}\n")

    # ── CLAUDE API CALL ───────────────────────────────────────────────────────
    def _get_response(self, user_input: str) -> str:
        user_msg = self._user_prompt(user_input)
        self.conversation_history.append({"role": "user", "content": user_msg})

        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=200,
            system=self._system_prompt(),
            messages=self.conversation_history,
        )

        reply = response.content[0].text.strip()
        self.conversation_history.append({"role": "assistant", "content": reply})
        return reply

    # ── MULTIMODAL HOOKS (architecture ready — plug in APIs here) ────────────
    def _generate_scene_image(self, scene_description: str):
        """
        Hook for image synthesis integration (e.g. Stable Diffusion, DALL-E).
        Called at scenario start or on key events.
        TODO: integrate image generation API
        """
        pass

    def _generate_patient_voice(self, text: str):
        """
        Hook for voice generation (e.g. ElevenLabs, Google TTS).
        Called when patient speaks.
        TODO: integrate TTS API
        """
        pass

    # ── PERFORMANCE SUMMARY ───────────────────────────────────────────────────
    def _print_summary(self):
        print("\n" + "=" * 55)
        print("   SIMULATION COMPLETE — PERFORMANCE REPORT")
        print("=" * 55)
        print(f"  Scenario     : {self.scenario['name']}")
        print(f"  Final Score  : {self.score}/100")
        print(f"  Turns Taken  : {self.turn}")
        print(f"  Interventions: {len(self.completed)}/{len(self.interventions)} completed")
        print("\n  Checklist:")
        for key, data in self.interventions.items():
            status = "✅" if key in self.completed else "❌"
            label = key.replace("_", " ").title()
            print(f"    {status}  {label}  (+{data['score']} pts)")
        missed = [k for k in self.interventions if k not in self.completed]
        if missed:
            print("\n  Missed steps:")
            for k in missed:
                print(f"    • {k.replace('_', ' ').title()}: {self.interventions[k].get('rationale', 'Key intervention')}")
        print("\n  Verdict:", end=" ")
        if self.score >= 85:
            print("🏆 Excellent — optimal management.")
        elif self.score >= self.scenario["passing_score"]:
            print("👍 Good — passed with key steps covered.")
        elif self.score >= 40:
            print("⚠️  Fair — significant gaps in management.")
        else:
            print("❌ Poor — critical steps missed. Patient outcome compromised.")
        print("=" * 55 + "\n")

    # ── MAIN LOOP ─────────────────────────────────────────────────────────────
    def run(self):
        p = self.patient
        vitals_str = " | ".join(f"{k}: {v}" for k, v in self.vitals.items())
        print("=" * 55)
        print(f"  SCENARIO : {self.scenario['name']}")
        print(f"  PATIENT  : {p['name']}, {p['age']}{p['gender'][0]}")
        print(f"  CC       : {p['complaint']}")
        print(f"  VITALS   : {vitals_str}")
        print("=" * 55)
        print("  Commands: 'vitals' | 'score' | 'history' | 'quit'\n")
        print(f"  {self.scenario['opening']}\n")

        while self.turn < self.scenario["max_turns"]:
            user_input = input("  YOU > ").strip()
            if not user_input:
                continue
            if user_input.lower() == "quit":
                break
            if user_input.lower() == "vitals":
                vs = " | ".join(f"{k}: {v}" for k, v in self.vitals.items())
                print(f"\n  📊 {vs}\n")
                continue
            if user_input.lower() == "score":
                print(f"\n  🏅 Score: {self.score}/100 | Interventions: {len(self.completed)}/{len(self.interventions)}\n")
                continue
            if user_input.lower() == "history":
                print("\n  📋 Your decisions so far:")
                for i, d in enumerate(self.decisions):
                    print(f"    {i+1}. {d}")
                print()
                continue

            self.turn += 1
            self._check_interventions(user_input)
            self.decisions.append(user_input)
            response = self._get_response(user_input)
            print(f"\n  SIMULATION:\n  {response}\n")

        self._print_summary()
