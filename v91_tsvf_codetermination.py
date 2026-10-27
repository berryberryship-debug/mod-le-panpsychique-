#!/usr/bin/env python3
"""
V91 — Co-détermination pré/post-sélection (TSVF).

Illustre la structure formelle du formalisme à deux vecteurs d'état :
une pré-sélection (passé), une post-sélection (futur), et un weak value
qui dépend des deux bornes.

ATTENTION : le TSVF est mathématiquement équivalent à la MQ standard.
Son interprétation rétrocausale est une lecture philosophique contestée,
non un consensus. Ce script illustre la structure, pas une ontologie.

Usage :
    python v91_tsvf_codetermination.py [--alpha 0.7853981633974483]
                                        [--beta 0.0]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

import numpy as np
from qutip import Qobj, basis, ket2dm, sigmaz


@dataclass(frozen=True)
class V91Result:
    """Résultat de la simulation V91."""

    psi_pre: Qobj
    psi_post: Qobj
    overlap: complex
    rho_present: Qobj
    weak_value_sigma_z: complex
    alpha: float
    beta: float


def build_state(alpha: float) -> Qobj:
    """Construit |psi(alpha)> = cos(alpha)|0> + sin(alpha)|1>."""
    if not (0 <= alpha <= np.pi / 2):
        raise ValueError(f"alpha doit être dans [0, pi/2], reçu {alpha}")
    return (np.cos(alpha) * basis(2, 0)
            + np.sin(alpha) * basis(2, 1)).unit()


def v91_tsvf_codetermination(
    alpha: float = np.pi / 4,
    beta: float = 0.0,
) -> V91Result:
    """
    Simule la co-détermination pré/post-sélection.

    Parameters
    ----------
    alpha : float
        Angle de la pré-sélection (rad), dans [0, pi/2].
    beta : float
        Angle de la post-sélection (rad), dans [0, pi/2].

    Returns
    -------
    V91Result
        Contient les états, l'overlap, la matrice reconfigurée
        et le weak value de sigma_z.
    """
    psi_pre = build_state(alpha)
    psi_post = build_state(beta)

    overlap = psi_post.overlap(psi_pre)  # <post|pre>
    if abs(overlap) < 1e-12:
        raise ValueError(
            "Overlap nul : pré et post-sélection orthogonales, "
            "reconfiguration indéfinie."
        )

    rho_pre = ket2dm(psi_pre)
    projector_post = psi_post * psi_post.dag()

    # Reconfiguration conditionnelle (formalisme ABL)
    rho_present = (rho_pre * projector_post) / abs(overlap) ** 2

    # Weak value d'un observable
    sigma_z = sigmaz()
    weak_value = (psi_post.dag() * sigma_z * psi_pre) / overlap

    return V91Result(
        psi_pre=psi_pre,
        psi_post=psi_post,
        overlap=overlap,
        rho_present=rho_present,
        weak_value_sigma_z=weak_value,
        alpha=alpha,
        beta=beta,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="V91 : co-détermination pré/post-sélection (TSVF)."
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=np.pi / 4,
        help="Angle de pré-sélection (rad). Défaut : pi/4.",
    )
    parser.add_argument(
        "--beta",
        type=float,
        default=0.0,
        help="Angle de post-sélection (rad). Défaut : 0.",
    )
    args = parser.parse_args()

    try:
        res = v91_tsvf_codetermination(alpha=args.alpha, beta=args.beta)
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 1

    print(f"V91 — TSVF (alpha={res.alpha:.4f}, beta={res.beta:.4f})")
    print(f"  Overlap <post|pre>       : {res.overlap:.6f}")
    print(f"  Weak value <sigma_z>_w   : {res.weak_value_sigma_z:.6f}")
    print(f"  Trace rho_present        : "
          f"{np.real(np.trace(res.rho_present)):.6f}")

    # Assertions de cohérence
    assert abs(res.overlap) > 1e-12, "Overlap ne doit pas être nul"
    trace_val = np.real(np.trace(res.rho_present))
    assert abs(trace_val - 1.0) < 1e-6, "Trace de rho_present doit être 1"

    print("V91 : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
