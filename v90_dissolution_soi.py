"""
V90 — Dissolution du Soi dans le Fond Onirique
S (Soi) intriqué avec E (environnement onirique).
Pureté locale de S décroît, pureté globale SE reste à 1.
"""

import numpy as np
from qutip import basis, tensor, ket2dm, ptrace


def purity(rho):
    return float(np.real(np.trace(rho @ rho)))


def v90_dissolution_soi(theta=np.pi / 4):
    """Construit un état intriqué S-E et mesure les puretés."""
    s0, s1 = basis(2, 0), basis(2, 1)
    e0, e1 = basis(2, 0), basis(2, 1)

    psi_se = (np.cos(theta) * tensor(s0, e0)
              + np.sin(theta) * tensor(s1, e1)).unit()

    rho_se = ket2dm(psi_se)
    rho_s = ptrace(rho_se, 0)  # garde S, trace E

    return {
        "rho_s": rho_s,
        "rho_se": rho_se,
        "purity_s": purity(rho_s),
        "purity_se": purity(rho_se),
        "theta": theta,
    }


if __name__ == "__main__":
    res = v90_dissolution_soi(theta=np.pi / 4)
    print(f"Pureté locale S   : {res['purity_s']:.4f}")   # ~0.5
    print(f"Pureté globale SE : {res['purity_se']:.4f}")   # 1.0
    assert abs(res["purity_s"] - 0.5) < 1e-6
    assert abs(res["purity_se"] - 1.0) < 1e-6
    print("V90 : OK")
