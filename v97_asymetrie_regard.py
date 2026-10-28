"""
V97 — L'Asymétrie du Regard (Sartre et Wigner's Friend)
Modélise deux subjectivités (Moi et Autre) comme un système quantique intriqué.
Montre que chacun ne peut voir que la trace partielle (l'apparence) de l'autre,
et que la pureté locale chute alors que la pureté globale (la réalité du couple)
reste pure.
"""

import numpy as np
from qutip import basis, tensor, ket2dm, ptrace

def run_asymetrie():
    print("--- V97 : L'Asymétrie du Regard ---")
    
    # 1. État global intriqué (Moi et Autre en interaction)
    # Un état de Bell : si je suis |0>, tu es |0>. Si je suis |1>, tu es |1>.
    # C'est la relation intime, l'enchevêtrement des libertés.
    psi_M = basis(2, 0)
    psi_A = basis(2, 0)
    
    etat_global = (tensor(basis(2, 0), basis(2, 0)) + tensor(basis(2, 1), basis(2, 1))).unit()
    rho_global = ket2dm(etat_global)
    
    # 2. Ce que je vois de l'Autre (Trace partielle sur M)
    # Je ne vois que sa "Plénitude" (matrice réduite), pas sa "Vacuité" (état global).
    rho_autre = ptrace(rho_global, 1)
    
    # 3. Ce que l'Autre voit de moi (Trace partielle sur A)
    rho_moi = ptrace(rho_global, 0)
    
    # 4. Métriques
    purete_globale = np.real((rho_global * rho_global).tr())
    purete_moi = np.real((rho_moi * rho_moi).tr())
    purete_autre = np.real((rho_autre * rho_autre).tr())
    
    print(f"Pureté globale (le couple) : {purete_globale:.4f}")
    print(f"Pureté locale de Moi       : {purete_moi:.4f}")
    print(f"Pureté locale de l'Autre   : {purete_autre:.4f}")
    print("Interprétation : Nous ne voyons mutuellement que des états mixtes (0.5),")
    print("car nos trames intérieures (états purs) sont intriquées et inaccessibles.")

if __name__ == "__main__":
    run_asymetrie()
