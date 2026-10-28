#!/usr/bin/env python3
"""
V90 + V91 couplés — Le Soi comme système ouvert avec mémoire temporelle.

Chaîne physique :
    1. Décohérence markovienne pure (déphasage) sur S          [héritage V89]
    2. Intrication contrôlée S–E via purification de l'état    [héritage V90]
    3. Post-sélection projective sur S et reconstruction      [héritage V91]

Ce module n'est plus un prototype pédagogique. Il fournit :
    - validation stricte des paramètres et des opérateurs,
    - diagnostics quantitatifs (pureté, fidélité, distance de trace, entropy),
    - reproducibility (seed optionnelle),
    - interface CLI et API utilisable en batch / notebook,
    - résultats structurés et sérialisables.

Dépendances : numpy, qutip ≥ 5.0
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import numpy as np
from qutip import (
    Qobj,
    basis,
    entropy_vn,
    fidelity,
    ket2dm,
    mesolve,
    ptrace,
    sigmaz,
    tensor,
    tracedist,
)


# ---------------------------------------------------------------------------
# Résultat structuré
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CoupledResult:
    """Conteneur immuable des quantités physiques produites par la chaîne."""

    # Paramètres
    gamma: float
    t_final: float
    n_steps: int

    # Métriques principales
    purity_s_before: float
    purity_s_after: float
    von_neumann_before: float
    von_neumann_after: float
    fidelity_to_post: float
    trace_distance_to_post: float
    overlap: complex
    overlap_abs2: float = field(init=False)

    # État final
    rho_present: Qobj

    # Diagnostics supplémentaires
    eigenvalues_rho_t: tuple[float, ...]
    dominant_eigenvalue: float
    trace_rho_present: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "overlap_abs2", abs(self.overlap) ** 2)

    def summary(self) -> dict[str, Any]:
        """Résumé sérialisable (sans les Qobj)."""
        return {
            "gamma": self.gamma,
            "t_final": self.t_final,
            "n_steps": self.n_steps,
            "purity_s_before": self.purity_s_before,
            "purity_s_after": self.purity_s_after,
            "von_neumann_before": self.von_neumann_before,
            "von_neumann_after": self.von_neumann_after,
            "fidelity_to_post": self.fidelity_to_post,
            "trace_distance_to_post": self.trace_distance_to_post,
            "overlap_real": float(np.real(self.overlap)),
            "overlap_imag": float(np.imag(self.overlap)),
            "overlap_abs2": self.overlap_abs2,
            "dominant_eigenvalue": self.dominant_eigenvalue,
            "eigenvalues_rho_t": list(self.eigenvalues_rho_t),
            "trace_rho_present": self.trace_rho_present,
        }

    def to_json(self, path: Optional[Path | str] = None, indent: int = 2) -> str:
        data = self.summary()
        text = json.dumps(data, indent=indent, ensure_ascii=False)
        if path is not None:
            Path(path).write_text(text, encoding="utf-8")
        return text


# ---------------------------------------------------------------------------
# Utilitaires physiques
# ---------------------------------------------------------------------------

def purity(rho: Qobj) -> float:
    """Tr(ρ²). Doit être dans [1/d, 1] pour un état physique de dimension d."""
    val = float(np.real((rho * rho).tr()))
    return val


def _assert_density_operator(rho: Qobj, name: str = "rho", tol: float = 1e-8) -> None:
    """Vérifie hermiticité, trace ≈ 1 et positivité (valeurs propres ≥ -tol)."""
    if not rho.isherm:
        raise ValueError(f"{name} n'est pas hermitien")
    tr = float(np.real(rho.tr()))
    if abs(tr - 1.0) > tol:
        raise ValueError(f"Tr({name}) = {tr:.6e} ≠ 1")
    evals = rho.eigenenergies()
    if np.any(evals < -tol):
        raise ValueError(
            f"{name} possède des valeurs propres négatives : {evals}"
        )


# ---------------------------------------------------------------------------
# Cœur de la simulation
# ---------------------------------------------------------------------------

def v90_v91_coupled(
    gamma: float = 0.1,
    t_max: float = 10.0,
    n_steps: int = 200,
    post_selection_state: Optional[Qobj] = None,
    seed: Optional[int] = None,
    options: Optional[dict] = None,
) -> CoupledResult:
    """
    Exécute la chaîne complète décohérence → intrication → post-sélection.

    Parameters
    ----------
    gamma :
        Taux de déphasage markovien (strictement positif).
    t_max :
        Horizon temporel de l'évolution markovienne.
    n_steps :
        Nombre de points de la grille temporelle (≥ 2).
    post_selection_state :
        État pur sur lequel on post-sélectionne (défaut |0⟩).
        Doit être un ket normalisé de dimension 2.
    seed :
        Graine pour toute source de hasard future (actuellement non utilisée
        car la dynamique est déterministe ; réservée pour extensions stochastiques).
    options :
        Dictionnaire d'options passées à mesolve (atol, rtol, method, …).

    Returns
    -------
    CoupledResult
        Objet contenant puretés, entropies, fidélité, distance de trace,
        overlap et l'état reconstruit après post-sélection.
    """
    # --- Validation des paramètres ---
    if gamma <= 0:
        raise ValueError(f"gamma doit être > 0, reçu {gamma}")
    if t_max <= 0:
        raise ValueError(f"t_max doit être > 0, reçu {t_max}")
    if n_steps < 2:
        raise ValueError(f"n_steps doit être ≥ 2, reçu {n_steps}")

    if seed is not None:
        np.random.seed(seed)

    if post_selection_state is None:
        psi_post = basis(2, 0)
    else:
        if not isinstance(post_selection_state, Qobj):
            raise TypeError("post_selection_state doit être un Qobj")
        if post_selection_state.type != "ket":
            raise ValueError("post_selection_state doit être un ket")
        if post_selection_state.shape[0] != 2:
            raise ValueError("post_selection_state doit être de dimension 2")
        psi_post = post_selection_state.unit()

    tlist = np.linspace(0.0, t_max, n_steps)
    solver_opts = options or {}

    # ------------------------------------------------------------------
    # Phase 1 — Décohérence markovienne pure (déphasage)
    # ------------------------------------------------------------------
    H = 0.5 * sigmaz()          # Hamiltonien libre (échelle d'énergie ħ=1)
    c_ops = [np.sqrt(gamma) * sigmaz()]   # canal de déphasage pur

    psi0 = (basis(2, 0) + basis(2, 1)).unit()
    result = mesolve(H, psi0, tlist, c_ops, e_ops=[], options=solver_opts)
    rho_t = result.states[-1]
    _assert_density_operator(rho_t, "rho_t")

    evals, evecs = rho_t.eigenstates()
    # Tri décroissant (QuTiP renvoie déjà ordonné croissant)
    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = [evecs[i] for i in order]
    psi_dominant = evecs[0]
    dominant_eval = float(evals[0])

    # ------------------------------------------------------------------
    # Phase 2 — Intrication avec l'environnement E (purification)
    # ------------------------------------------------------------------
    # Purification standard de l'état mixte ρ_t :
    #   |Ψ_SE⟩ = Σ_k √λ_k |ψ_k⟩_S ⊗ |k⟩_E
    # On utilise uniquement les deux vecteurs propres (dim S = 2).
    e0, e1 = basis(2, 0), basis(2, 1)
    amp0 = np.sqrt(max(evals[0], 0.0))
    amp1 = np.sqrt(max(evals[1], 0.0))

    psi_se = (amp0 * tensor(evecs[0], e0) + amp1 * tensor(evecs[1], e1)).unit()
    rho_se = ket2dm(psi_se)
    _assert_density_operator(rho_se, "rho_se")

    # Réduction sur S
    rho_s_reduced = ptrace(rho_se, 0)
    _assert_density_operator(rho_s_reduced, "rho_s_reduced")

    # ------------------------------------------------------------------
    # Phase 3 — Post-sélection projective
    # ------------------------------------------------------------------
    overlap = psi_post.overlap(psi_dominant)
    abs2 = abs(overlap) ** 2

    if abs2 < 1e-14:
        raise RuntimeError(
            "Overlap |⟨post|dominant⟩|² < 1e-14 : la post-sélection "
            "est numériquement indéfinie. Choisir un autre état de post-sélection "
            "ou un régime de décohérence moins avancé."
        )

    projector = psi_post * psi_post.dag()
    # Formule de post-sélection : ρ' = P ρ P / Tr(P ρ)
    rho_present = (projector * rho_s_reduced * projector) / abs2
    _assert_density_operator(rho_present, "rho_present")

    # ------------------------------------------------------------------
    # Diagnostics
    # ------------------------------------------------------------------
    pur_before = purity(rho_s_reduced)
    pur_after = purity(rho_present)
    S_before = float(entropy_vn(rho_s_reduced, base=np.e))
    S_after = float(entropy_vn(rho_present, base=np.e))
    fid = float(fidelity(rho_present, ket2dm(psi_post)))
    tdist = float(tracedist(rho_present, ket2dm(psi_post)))
    tr_present = float(np.real(rho_present.tr()))

    return CoupledResult(
        gamma=gamma,
        t_final=t_max,
        n_steps=n_steps,
        purity_s_before=pur_before,
        purity_s_after=pur_after,
        von_neumann_before=S_before,
        von_neumann_after=S_after,
        fidelity_to_post=fid,
        trace_distance_to_post=tdist,
        overlap=complex(overlap),
        rho_present=rho_present,
        eigenvalues_rho_t=tuple(float(e) for e in evals),
        dominant_eigenvalue=dominant_eval,
        trace_rho_present=tr_present,
    )


# ---------------------------------------------------------------------------
# Interface en ligne de commande
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "V90+V91 couplés — décohérence markovienne → intrication S–E "
            "→ post-sélection projective."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--gamma", type=float, default=0.1,
                   help="Taux de déphasage markovien")
    p.add_argument("--t-max", type=float, default=10.0,
                   help="Temps final de l'évolution")
    p.add_argument("--n-steps", type=int, default=200,
                   help="Nombre de pas temporels")
    p.add_argument("--seed", type=int, default=None,
                   help="Graine aléatoire (réservée aux extensions stochastiques)")
    p.add_argument("--json", type=str, default=None,
                   help="Chemin de sortie JSON (optionnel)")
    p.add_argument("--quiet", action="store_true",
                   help="N'affiche que le résumé minimal")
    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        res = v90_v91_coupled(
            gamma=args.gamma,
            t_max=args.t_max,
            n_steps=args.n_steps,
            seed=args.seed,
        )
    except (ValueError, RuntimeError, TypeError) as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        return 1

    # Assertions de cohérence physiques (tolérances numériques réalistes)
    assert 0.5 - 1e-8 <= res.purity_s_before <= 1.0 + 1e-8, (
        f"Pureté avant hors bornes : {res.purity_s_before}"
    )
    assert abs(res.trace_rho_present - 1.0) < 1e-8, (
        f"Trace(rho_present) = {res.trace_rho_present}"
    )
    assert res.purity_s_after >= res.purity_s_before - 1e-8, (
        "La post-sélection ne peut pas diminuer la pureté"
    )

    if not args.quiet:
        print(f"V90+V91 couplés  (γ={res.gamma}, t={res.t_final}, steps={res.n_steps})")
        print(f"  Pureté S avant post-sélection : {res.purity_s_before:.8f}")
        print(f"  Pureté S après  post-sélection : {res.purity_s_after:.8f}")
        print(f"  Entropie de von Neumann avant  : {res.von_neumann_before:.8f}")
        print(f"  Entropie de von Neumann après  : {res.von_neumann_after:.8f}")
        print(f"  Fidélité à |post⟩              : {res.fidelity_to_post:.8f}")
        print(f"  Distance de trace à |post⟩     : {res.trace_distance_to_post:.8f}")
        print(f"  Overlap ⟨post|dominant⟩        : {res.overlap:.8f}")
        print(f"  |overlap|²                     : {abs(res.overlap)**2:.8f}")
        print(f"  Valeur propre dominante        : {res.dominant_eigenvalue:.8f}")
        print(f"  Spectre ρ(t)                   : {res.eigenvalues_rho_t}")

    if args.json:
        res.to_json(args.json)
        if not args.quiet:
            print(f"  → Résultats écrits dans {args.json}")

    if not args.quiet:
        print("V90+V91 couplés : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
