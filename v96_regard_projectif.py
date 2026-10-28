"""
V96 — Le Regard comme mesure projective (Sartre)
Modélise le passage du "Pour-Soi" (superposition, liberté) à l'"En-Soi"
(état figé, objet) par l'application d'un projecteur (le Regard de l'Autre).
Montre la destruction des cohérences (termes hors-diagonale).
"""

import numpy as np
from qutip import basis, ket2dm, sigmaz, sigmax, Qobj

def run_regard_projectif():
    print("--- V96 : Le Regard comme mesure projective ---")
    
    # 1. État initial : "Pour-Soi" (Superposition |+>)
    # C'est la liberté, la trame intérieure non figée.
    psi_pour_soi = (basis(2, 0) + basis(2, 1)).unit()
    rho_avant = ket2dm(psi_pour_soi)
    
    # 2. Le Regard de l'Autre (Projecteur sur un état spécifique, ex: |0>)
    # L'Autre me fige dans une catégorie ("tu es ceci").
    psi_regard = basis(2, 0)
    P_regard = psi_regard * psi_regard.dag()
    
    # 3. Application du Regard (Effondrement)
    # Formule de la mesure projective : rho' = P * rho * P / Tr(P * rho)
    proba = (rho_avant * P_regard).tr()
    rho_apres = (P_regard * rho_avant * P_regard) / proba
    
    # 4. Métriques
    # Pureté avant (Vacuité) et après (Plénitude figée)
    purete_avant = np.real((rho_avant * rho_avant).tr())
    purete_apres = np.real((rho_apres * rho_apres).tr())
    
    # Cohérences (les termes hors-diagonale qui représentent la liberté)
    coherence_avant = np.abs(rho_avant[0, 1])
    coherence_apres = np.abs(rho_apres[0, 1])
    
    print(f"Pureté avant le Regard : {purete_avant:.4f}")
    print(f"Pureté après le Regard : {purete_apres:.4f}")
    print(f"Cohérence avant       : {coherence_avant:.4f} (Liberté)")
    print(f"Cohérence après       : {coherence_apres:.4f} (Aliénation)")
    print("Interprétation : L'Autre m'a objectivé. Ma trame intérieure (cohérence) est détruite.")

if __name__ == "__main__":
    run_regard_projectif()
