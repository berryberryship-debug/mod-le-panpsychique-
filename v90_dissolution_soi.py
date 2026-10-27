#!/usr/bin/env python3
"""
V90 — Dissolution du Soi dans le Fond Onirique.

Modélise l'intrication entre un système "Soi" (S) et un environnement
"onirique" (E). La pureté locale de S décroît vers le mélange maximal
tandis que la pureté globale SE reste à 1.0 : l'information n'est pas
détruite, elle est délocalisée dans l'intrication.

Usage :
    python v90_dissolution_soi.py [--theta 0.7853981633974483]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

import numpy as np
from qutip import Qobj, basis, ket2dm, ptrace, tensor


@dataclass(frozen=True)
class V90Result:
    """Résultat de la simulation V90."""

    rho_s: Qobj
    rho_se: Qobj
    purity_s: float
    purity_se: float
    theta: float


def purity(rho: Qobj) -> float:
    """Calcule Tr(rho^2), la pureté d'une matrice densité."""
    return float(np.real(np.trace(rho @ rho)))


def build_entangled_state(theta: float) -> Qobj:
    """Construit un état Bell-like paramétré par theta."""
    if not (0 <= theta <= np.pi / 2):
        raise ValueError(f"theta doit être dans [0, pi/2], reçu {theta}")

    s0, s1 = basis(2, 0), basis(2, 1)
    e0, e1 = basis(2, 0), basis(2, 1)

    return (
        np.cos(theta) * tensor(s0, e0)
        + np.sin(theta) * tensor(s1, e1)
    ).unit()


def v90_dissolution_soi(theta: float = np.pi / 4) -> V90Result:
    """
    Simule l'intrication S-E et mesure les puretés.

    Parameters
    ----------
    theta : float
        Angle d'intrication, dans [0, pi/2].
        theta = 0 : état produit (pas d'intrication).
        theta = pi/4 : intrication maximale (Bell state).

    Returns
    -------
    V90Result
        Contient les matrices densité et les puretés.
    """
    psi_se = build_entangled_state(theta)
    rho_se = ket2dm(psi_se)
    rho_s = ptrace(rho_se, 0)  # garde S, trace E

    return V90Result(
        rho_s=rho_s,
        rho_se=rho_se,
        purity_s=purity(rho_s),
        purity_se=purity(rho_se),
        theta=theta,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="V90 : dissolution du Soi par intrication S-E."
    )
    parser.add_argument(
        "--theta",
        type=float,
        default=np.pi / 4,
        help="Angle d'intrication (rad), dans [0, pi/2]. Défaut : pi/4.",
    )
    args = parser.parse_args()

    try:
        res = v90_dissolution_soi(theta=args.theta)
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        return 1

    print(f"V90 — Dissolution du Soi (theta = {res.theta:.4f} rad)")
    print(f"  Pureté locale S   : {res.purity_s:.6f}")
    print(f"  Pureté globale SE : {res.purity_se:.6f}")

    # Assertions de cohérence
    assert 0.5 <= res.purity_s <= 1.0, "Pureté locale hors bornes"
    assert abs(res.purity_se - 1.0) < 1e-6, "Pureté globale doit être 1.0"

    if abs(res.theta - np.pi / 4) < 1e-6:
        assert abs(res.purity_s - 0.5) < 1e-6, (
            "À theta=pi/4, la pureté locale doit être 0.5"
        )

    print("V90 : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
