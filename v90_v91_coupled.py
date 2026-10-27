#!/usr/bin/env python3
"""
V90 + V91 couplés — Le Soi comme système ouvert avec mémoire temporelle.

Chaîne complète :
    1. Décohérence markovienne (héritage V89)
    2. Intrication avec E (héritage V90)
    3. Post-sélection (héritage V91)

Usage :
    python v90_v91_coupled.py [--gamma 0.1] [--t-max 10.0] [--n-steps 200]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

import numpy as np
from qutip import Qobj, basis, ket2dm, mesolve, ptrace, sigmaz, tensor


@dataclass(frozen=True)
class CoupledResult:
    """Résultat de la simulation couplée V90+V91."""

    purity_s_before: float
    purity_s_after: float
    overlap: complex
    rho_present: Qobj
    gamma: float
    t_final: float


def purity(rho: Qobj) -> float:
    """Calcule Tr(rho^2)."""
    return float(np.real(np.trace(rho @ rho)))


def v90_v91_coupled(
    gamma: float = 0.1,
    t_max: float = 10.0,
    n_steps: int = 200,
) -> CoupledResult:
    """
    Simule la chaîne complète : décohérence → intrication → post-sélection.

    Parameters
    ----------
    gamma : float
        Taux de déphasage markovien. Doit être strictement positif.
    t_max : float
        Temps final de la simulation.
    n_steps : int
        Nombre de pas de temps.

    Returns
    -------
    CoupledResult
        Contient les puretés avant/après post-sélection,
        l'overlap, et la matrice finale.
    """
    if gamma <= 0:
        raise ValueError(f"gamma doit être strictement positif, reçu {gamma}")
    if t_max <= 0:
        raise ValueError(f"t_max doit être strictement positif, reçu {t_max}")
    if n_steps < 2:
        raise ValueError(f"n_steps doit être >= 2, reçu {n_steps}")

    tlist = np.linspace(0, t_max, n_steps)

    # --- Phase 1 : décohérence markovienne (V89) ---
    H = sigmaz()
    c_ops = [np.sqrt(gamma) * sigmaz()]  # déphasage pur
    psi0 = (basis(2, 0) + basis(2, 1)).unit()

    result = mesolve(H, psi0, tlist, c_ops, [])
    rho_t = result.states[-1]

    # --- Phase 2 : intrication avec E (V90) ---
    e0, e1 = basis(2, 0), basis(2, 1)
    evals, evecs = rho_t.eigenstates()
    psi_dominant = evecs[-1]  # vecteur propre de plus grande valeur propre

    psi_se = (
        np.sqrt(0.5) * tensor(psi_dominant, e0)
        + np.sqrt(0.5) * tensor(basis(2, 1), e1)
    ).unit()
    rho_se = ket2dm(psi_se)

    # --- Phase 3 : post-sélection (V91) ---
    psi_post = basis(2, 0)
    rho_s_reduced = ptrace(rho_se, 0)
    overlap = psi_post.overlap(psi_dominant)

    if abs(overlap) < 1e-12:
        raise ValueError(
            "Overlap nul entre post-sélection et état dominant : "
            "reconfiguration indéfinie."
        )

    projector_post = psi_post * psi_post.dag()
    rho_present = (rho_s_reduced * projector_post) / abs(overlap) ** 2

    return CoupledResult(
        purity_s_before=purity(rho_s_reduced),
        purity_s_after=purity(rho_present),
        overlap=overlap,
        rho_present=rho_present,
        gamma=gamma,
        t_final=t_max,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="V90+V91 couplés : décohérence → intrication → post-sélection."
    )
    parser.add_argument(
        "--gamma",
        type=float,
        default=0.1,
        help="Taux de déphasage markovien. Défaut : 0.1.",
    )
    parser.add_argument(
        "--t-max",
        type=float,
        default=10.0,
        help="Temps final de la simulation. Défaut : 10.0.",
    )
    parser.add_argument(
        "--n-steps",
        type=int,
        default=200,
        help="Nombre de pas de temps. Défaut : 200.",
    )
    args = parser.parse_args()

    try:
        res = v90_v91_coupled(
            gamma=args.gamma,
            t_max=args.t_max,
            n_steps=args.n_steps,
        )
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 1

    print(f"V90+V91 couplés (gamma={res.gamma}, t_final={res.t_final})")
    print(f"  Pureté S avant post-sélection : {res.purity_s_before:.6f}")
    print(f"  Pureté S après post-sélection : {res.purity_s_after:.6f}")
    print(f"  Overlap <post|dominant>       : {res.overlap:.6f}")

    # Assertions de cohérence
    assert 0.5 <= res.purity_s_before <= 1.0, (
        "Pureté avant post-sélection hors bornes"
    )
    trace_val = np.real(np.trace(res.rho_present))
    assert abs(trace_val - 1.0) < 1e-6, "Trace de rho_present doit être 1"

    print("V90+V91 couplés : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
