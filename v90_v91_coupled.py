"""
V90 + V91 couplés — Le Soi comme système ouvert avec mémoire temporelle.
Chaîne : décohérence (V89) → intrication (V90) → post-sélection (V91).
"""

import numpy as np
from qutip import basis, tensor, ket2dm, ptrace, sigmaz, mesolve


def purity(rho):
    return float(np.real(np.trace(rho @ rho)))


def v90_v91_coupled(gamma=0.1, tlist=None):
    """
    Phase 1 : décohérence markovienne (héritage V89)
    Phase 2 : intrication avec E (héritage V90)
    Phase 3 : post-sélection (héritage V91)
    """
    if tlist is None:
        tlist = np.linspace(0, 10, 200)

    # --- Phase 1 : décohérence markovienne ---
    H = sigmaz()
    c_ops = [np.sqrt(gamma) * sigmaz()]  # déphasage pur
    psi0 = (basis(2, 0) + basis(2, 1)).unit()

    result = mesolve(H, psi0, tlist, c_ops, [])
    rho_t = result.states[-1]

    # --- Phase 2 : intrication avec E ---
    e0, e1 = basis(2, 0), basis(2, 1)
    evals, evecs = rho_t.eigenstates()
    psi_dominant = evecs[-1]  # vecteur propre dominant

    psi_se = (np.sqrt(0.5) * tensor(psi_dominant, e0)
              + np.sqrt(0.5) * tensor(basis(2, 1), e1)).unit()
    rho_se = ket2dm(psi_se)

    # --- Phase 3 : post-sélection ---
    psi_post = basis(2, 0)
    rho_s_reduced = ptrace(rho_se, 0)
    overlap = psi_post.overlap(psi_dominant)

    projector_post = psi_post * psi_post.dag()
    rho_present = (rho_s_reduced * projector_post) / abs(overlap) ** 2

    return {
        "purity_s_before": purity(rho_s_reduced),
        "purity_s_after": purity(rho_present),
        "overlap": overlap,
        "rho_present": rho_present,
        "gamma": gamma,
    }


if __name__ == "__main__":
    res = v90_v91_coupled(gamma=0.1)
    print(f"Pureté S avant post-sélection : {res['purity_s_before']:.4f}")
    print(f"Pureté S après post-sélection : {res['purity_s_after']:.4f}")
    print(f"Overlap <post|dominant>       : {res['overlap']:.4f}")
