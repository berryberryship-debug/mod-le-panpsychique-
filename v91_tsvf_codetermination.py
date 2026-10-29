import numpy as np
from qutip import basis, sigmaz

def calculer_valeur_faible(alpha):
    # alpha négatif autorisé pour avoir un recouvrement faible
    psi_pre = (basis(2, 0) + basis(2, 1)).unit()
    psi_post = (np.cos(alpha) * basis(2, 0) + np.sin(alpha) * basis(2, 1)).unit()
    
    overlap = psi_post.overlap(psi_pre)
    
    if abs(overlap) < 1e-12:
        return np.nan, overlap
        
    A = sigmaz()
    A_w = (psi_post.dag() * A * psi_pre)[0, 0] / overlap
    
    return np.real(A_w), np.real(overlap)

if __name__ == "__main__":
    print("=== V91 : TSVF et Valeur Faible ===")
    # Un angle proche de -pi/4 donne un recouvrement très faible
    alpha = -np.pi/4 + 0.05 
    A_w, overlap = calculer_valeur_faible(alpha)
    
    print(f"Angle : {alpha:.4f} | Recouvrement : {overlap:.4f} | Valeur faible : {A_w:.4f}")
    
    # ASSERTIONS DYNAMIQUES
    assert abs(overlap) > 1e-5, "ÉCHEC : Recouvrement trop faible."
    assert abs(A_w) > 1.0, f"ÉCHEC : Valeur faible ({A_w:.4f}) dans l'intervalle classique."
    
    print("-> SUCCÈS : Valeur faible anomale détectée.")
