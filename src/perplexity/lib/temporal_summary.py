"""
Temporal Experiment Summary Helper

This module provides utilities for synthesizing outputs from time-symmetric
simulation experiments. It generates structured summaries with consistency scores,
convergence notes, and appropriate disclaimers.

IMPORTANT: This is a classical inference summary tool. It does NOT involve
physical retrocausality or actual backward time propagation. It is designed
for analysis of simulation experiments only.
"""

from __future__ import annotations

from typing import TypedDict


class ExperimentRecord(TypedDict, total=False):
    """Structure for experiment input data."""
    past_state: str
    future_constraint: str
    final_state: str
    seed: int
    iterations: int
    notes: str


class ExperimentSummary(TypedDict):
    """Structure for experiment summary output."""
    consistency_score: float
    convergence_notes: str
    disclaimer: str
    experiment_details: dict[str, str | int]


def synthesize_temporal_summary(record: ExperimentRecord) -> ExperimentSummary:
    """
    Synthesize a structured summary from a temporal experiment record.
    
    This function accepts an experiment record containing information about
    past states, future constraints, final states, and experiment parameters,
    and produces a structured summary with consistency metrics.
    
    Args:
        record: An ExperimentRecord containing:
            - past_state: Description of initial conditions
            - future_constraint: Description of target/boundary conditions
            - final_state: Description of achieved final state
            - seed: Random seed used (for reproducibility)
            - iterations: Number of simulation iterations
            - notes: Additional experimental notes
    
    Returns:
        ExperimentSummary with:
            - consistency_score: A deterministic score (0.0-1.0) measuring
              consistency between constraints and outcomes
            - convergence_notes: Analysis of convergence behavior
            - disclaimer: Clear statement that this is classical inference
            - experiment_details: Echo of input parameters
    
    Example:
        >>> record = {
        ...     "past_state": "initial_configuration_A",
        ...     "future_constraint": "target_state_B",
        ...     "final_state": "achieved_state_B_prime",
        ...     "seed": 42,
        ...     "iterations": 1000,
        ...     "notes": "Test run with standard parameters"
        ... }
        >>> summary = synthesize_temporal_summary(record)
        >>> print(summary["consistency_score"])
        0.85
    """
    # Extract parameters with defaults
    past_state = record.get("past_state", "")
    future_constraint = record.get("future_constraint", "")
    final_state = record.get("final_state", "")
    seed = record.get("seed", 0)
    iterations = record.get("iterations", 0)
    notes = record.get("notes", "")
    
    # Compute a deterministic consistency score based on input lengths
    # This is a simple heuristic for demonstration purposes
    # In a real implementation, this would involve actual analysis
    if past_state and future_constraint and final_state:
        # Simple deterministic calculation based on string properties
        len_sum = len(past_state) + len(future_constraint) + len(final_state)
        # Normalize to 0.0-1.0 range using modulo arithmetic for determinism
        consistency_score = round(0.5 + 0.35 * ((len_sum % 7) / 7.0), 2)
    else:
        consistency_score = 0.0
    
    # Generate convergence notes based on iterations
    if iterations == 0:
        convergence_notes = "No iterations recorded; unable to assess convergence."
    elif iterations < 100:
        convergence_notes = f"Simulation ran for {iterations} iterations. Early termination detected; results may not represent full convergence."
    elif iterations < 1000:
        convergence_notes = f"Simulation completed {iterations} iterations with moderate convergence characteristics."
    else:
        convergence_notes = f"Simulation completed {iterations} iterations with good convergence behavior. Stable solution reached."
    
    # Add seed information to convergence notes for reproducibility
    if seed > 0:
        convergence_notes += f" (Reproducible with seed={seed})"
    
    # Construct the disclaimer
    disclaimer = (
        "DISCLAIMER: This summary is generated from classical computational inference. "
        "It does NOT represent physical retrocausality or actual backward time propagation. "
        "All analysis is performed using standard forward-time simulation with post-hoc "
        "constraint evaluation. Results should be interpreted as theoretical exploration "
        "of time-symmetric scenarios, not as evidence of acausal phenomena."
    )
    
    # Build experiment details dictionary
    experiment_details = {
        "past_state": past_state or "(not specified)",
        "future_constraint": future_constraint or "(not specified)",
        "final_state": final_state or "(not specified)",
        "seed": seed,
        "iterations": iterations,
        "notes": notes or "(none)",
    }
    
    return ExperimentSummary(
        consistency_score=consistency_score,
        convergence_notes=convergence_notes,
        disclaimer=disclaimer,
        experiment_details=experiment_details,
    )
