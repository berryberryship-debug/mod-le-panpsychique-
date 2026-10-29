"""
V91 — Co-détermination TSVF et Valeurs Faibles.
Calcule la valeur faible de sigma_z et vérifie l'effet anomal.
"""
import numpy as np
from qutip import basis, sigmaz

def calculer_valeur_faible(alpha):
    """
    alpha : angle de post-sélection.
    Pré-sélection : |+> = (|0> + |1>) / sqrt(2)
    Post-sélection : cos(alpha)|0> + sin(alpha)|1>
    """
    # Pré-sélection
    psi_pre = (basis(2, 0) + basis(2, 1)).unit()
    
    # Post-sélection
    psi_post = (np.cos(alpha) * basis(2, 0) + np.sin(alpha) * basis(2, 1)).unit()
    
    # Recouvrement
    overlap = psi_post.overlap(psi_pre)
    
    # Sécurité si le recouvrement est trop faible
    if abs(overlap) < 1e-10:
        return np.nan, overlap
        
    # Opérateur A = sigma_z
    A = sigmaz()
    
    # Valeur faible : A_w = <post| A |pre> / <post|pre>
    A_w = (psi_post.dag() * A * psi_pre)[0, 0] / overlap
    
    return np.real(A_w), np.real(overlap)

if __name__ == "__main__":
    print("=== V91 : TSVF et Valeur Faible (Assertions Dynamiques) ===")
    
    # On choisit un angle proche de -pi/4 pour rendre le recouvrement petit
    # et faire sortir la valeur faible de l'intervalle [-1, 1]
    alpha = -np.pi/4 + 0.05 
    
    A_w, overlap = calculer_valeur_faible(alpha)
    
    print(f"Angle de post-sélection : {alpha:.4f} rad")
    print(f"Recouvrement            : {overlap:.4f}")
    print(f"Valeur faible <sigma_z> : {A_w:.4f}")
    
    # ASSERTIONS DYNAMIQUES
    assert abs(overlap) > 1e-5, "ÉCHEC : Recouvrement quasi nul."
    assert abs(A_w) > 1.0, f"ÉCHEC : La valeur faible ({A_w:.4f}) ne sort pas de l'intervalle [-1, 1]."
    
    print("-> SUCCÈS : La valeur faible est anomale (hors intervalle spectral).")
