"""
V98 — La Rencontre comme Valeur Faible (TSVF sartrien)
Modélise l'interaction entre ma "liberté passée" (pré-sélection)
et l'"image que l'Autre me force à projeter" (post-sélection).
Calcule la valeur faible de mon identité.
"""

import numpy as np
from qutip import basis, sigmaz, sigmax

def run_rencontre_tsvf():
    print("--- V98 : La Rencontre comme Valeur Faible ---")
    
    # 1. Pré-sélection (Mon passé, ma liberté intérieure)
    # Je suis dans un état de superposition |+>
    psi_pre = (basis(2, 0) + basis(2, 1)).unit()
    
    # 2. Post-sélection (Le rôle que l'Autre m'impose, le Regard)
    # L'Autre m'attend à un endroit précis (ex: |0>)
    psi_post = basis(2, 0)
    
    # 3. Observable (Mon identité, mes choix)
    A = sigmaz() # Observons l'axe Z (la décision)
    
    # 4. Calcul de la valeur faible (Weak Value)
    # A_w = <post| A |pre> / <post|pre>
    overlap = psi_post.overlap(psi_pre)
    numerateur = psi_post.dag() * A * psi_pre
    valeur_faible = numerateur / overlap
    
    # 5. Métriques
    print(f"Overlap (chevauchement des attentes) : {overlap:.4f}")
    print(f"Valeur faible de mon identité        : {valeur_faible:.4f}")
    
    # On peut calculer la pureté reconstruite (la trace partielle de ma réalité)
    # Cette valeur faible peut être "anomale" (sortir de -1, 1).
    if np.abs(valeur_faible) > 1.0:
        print("→ Valeur faible anomale : L'Autre me perçoit de manière biaisée")
        print("  (Il me voit plus que ce que je suis, ou moins que ce que je suis).")
    else:
        print("→ Valeur faible standard : La rencontre est conforme aux attentes.")

if __name__ == "__main__":
    run_rencontre_tsvf()
