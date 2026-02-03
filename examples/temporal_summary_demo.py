#!/usr/bin/env python3
"""
Temporal Experiment Summary Demo

This script demonstrates the use of the temporal_summary helper module
to analyze time-symmetric simulation experiments. It uses fixed inputs
to ensure deterministic, reproducible output.

Usage:
    python examples/temporal_summary_demo.py
"""

import sys
from pathlib import Path

# Add src to path to import the module directly
# This avoids importing the full perplexity package with its dependencies
lib_path = Path(__file__).parent.parent / "src" / "perplexity" / "lib"
sys.path.insert(0, str(lib_path))

from temporal_summary import synthesize_temporal_summary


def main():
    """Run the temporal summary demo with fixed inputs."""
    
    print("=" * 70)
    print("Temporal Experiment Summary Demo")
    print("=" * 70)
    print()
    
    # Example 1: Complete experiment record
    print("Example 1: Complete Experiment")
    print("-" * 70)
    
    experiment_1 = {
        "past_state": "quantum_system_ground_state",
        "future_constraint": "excited_state_target_energy_5.2eV",
        "final_state": "excited_state_achieved_energy_5.18eV",
        "seed": 42,
        "iterations": 1500,
        "notes": "Standard perturbation analysis with time-symmetric boundary conditions"
    }
    
    summary_1 = synthesize_temporal_summary(experiment_1)
    
    print(f"Consistency Score: {summary_1['consistency_score']}")
    print(f"\nConvergence Notes:")
    print(f"  {summary_1['convergence_notes']}")
    print(f"\nExperiment Details:")
    for key, value in summary_1['experiment_details'].items():
        print(f"  {key}: {value}")
    print(f"\n{summary_1['disclaimer']}")
    print()
    
    # Example 2: Minimal experiment record
    print("=" * 70)
    print("Example 2: Minimal Experiment")
    print("-" * 70)
    
    experiment_2 = {
        "past_state": "initial",
        "future_constraint": "target",
        "final_state": "result",
        "seed": 123,
        "iterations": 50,
        "notes": "Quick test run"
    }
    
    summary_2 = synthesize_temporal_summary(experiment_2)
    
    print(f"Consistency Score: {summary_2['consistency_score']}")
    print(f"\nConvergence Notes:")
    print(f"  {summary_2['convergence_notes']}")
    print(f"\nExperiment Details:")
    for key, value in summary_2['experiment_details'].items():
        print(f"  {key}: {value}")
    print()
    
    # Example 3: Experiment with high iterations
    print("=" * 70)
    print("Example 3: High-Iteration Experiment")
    print("-" * 70)
    
    experiment_3 = {
        "past_state": "classical_harmonic_oscillator_at_rest",
        "future_constraint": "maximum_displacement_at_t_10s",
        "final_state": "oscillator_at_maximum_displacement",
        "seed": 2024,
        "iterations": 10000,
        "notes": "Extended simulation for high-precision convergence analysis"
    }
    
    summary_3 = synthesize_temporal_summary(experiment_3)
    
    print(f"Consistency Score: {summary_3['consistency_score']}")
    print(f"\nConvergence Notes:")
    print(f"  {summary_3['convergence_notes']}")
    print()
    
    print("=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
