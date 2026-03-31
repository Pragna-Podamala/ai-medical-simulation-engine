"""
Medical Scenario Simulation Agent v2
Author: Podamala Pragna
GitHub: github.com/Podamala-Pragna

Entry point — run this to start the simulation.
Powered by Anthropic Claude API.
"""

from agents.simulation_engine import SimulationEngine
from scenarios.stemi import STEMI_SCENARIO
from scenarios.sepsis import SEPSIS_SCENARIO
from scenarios.anaphylaxis import ANAPHYLAXIS_SCENARIO

SCENARIOS = {
    "1": ("STEMI (Heart Attack)", STEMI_SCENARIO),
    "2": ("Sepsis (Infection Shock)", SEPSIS_SCENARIO),
    "3": ("Anaphylaxis (Severe Allergic Reaction)", ANAPHYLAXIS_SCENARIO),
}

def main():
    print("\n" + "=" * 55)
    print("   🏥  MEDICAL SIMULATION AGENT v2 — ER TRAINING")
    print("   Powered by Anthropic Claude")
    print("=" * 55)
    print("\n  Choose a scenario:")
    for key, (name, _) in SCENARIOS.items():
        print(f"    [{key}] {name}")

    choice = input("\n  Enter 1, 2, or 3: ").strip()
    if choice not in SCENARIOS:
        print("  Invalid choice. Defaulting to STEMI.")
        choice = "1"

    name, scenario = SCENARIOS[choice]
    print(f"\n  Loading: {name}...\n")

    engine = SimulationEngine(scenario)
    engine.run()

if __name__ == "__main__":
    main()
