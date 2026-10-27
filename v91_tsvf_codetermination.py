"""
V91 — Co-détermination pré/post-sélection (TSVF)
Pré-sélection (passé) + post-sélection (futur)
→ reconfiguration formelle de la description du présent.
Note : illustre la structure formelle du TSVF,
pas une rétrocausalité ontologique.
"""

import numpy as np
from qutip import basis, ket2dm, sigmaz


def v91_tsvf_codetermination():
    """Pré-sélection |+>, post-sélection |0>, weak value de sigma_z."""
    psi_pre = (basis(2, 0) + basis(2, 1)).unit()   # |+>
    psi_post = basis(2, 0)                          # |0>

    overlap = psi_post.overlap(psi_pre)             # <post|pre>

    rho_pre = ket2dm(psi_pre)
    projector_post = psi_post * psi_post.dag()

    # Reconfiguration conditionnelle (formalisme ABL)
    rho_present = (rho_pre * projector_post) / abs(overlap) ** 2

    # Weak value d'un observable
    sigma_z = sigmaz()
    weak_value = (psi_post.dag() * sigma_z * psi_pre) / overlap

    return {
        "psi_pre": psi_pre,
        "psi_post": psi_post,
        "overlap": overlap,
        "rho_present": rho_present,
        "weak_value_sigma_z": weak_value,
    }


if __name__ == "__main__":
    res = v91_tsvf_codetermination()
    print(f"Overlap <post|pre>     : {res['overlap']:.4f}")
    print(f"Weak value <sigma_z>_w : {res['weak_value_sigma_z']:.4f}")
    print(f"Trace rho_present      : {np.real(np.trace(res['rho_present'])):.4f}")
