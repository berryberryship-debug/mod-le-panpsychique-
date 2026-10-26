import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

# Paramètres
T = 20.0
N = 400
dt = T / N
gammas = [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]

# Matrices de Pauli
sz = np.array([[1, 0], [0, -1]], dtype=complex)

# ÉTAT INITIAL CORRIGÉ : Superposition |+> (indispensable pour voir le déphasage)
rho_ideal = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)

def bures_fidelity_uhlmann(rho, sigma):
    """
    Calcule la fidélité d'Uhlmann (racine de Bures).
    F = Tr(sqrt(sqrt(rho) * sigma * sqrt(rho)))
    """
    sqrt_rho = sqrtm(rho)
    inner = sqrtm(sqrt_rho @ sigma @ sqrt_rho)
    # On retourne la trace SANS le carré (convention du document)
    return np.real(np.trace(inner))

def run_simulation():
    results = []
    
    for gamma in gammas:
        rho = np.copy(rho_ideal)
        
        # Évolution sous l'équation de Lindblad (déphasage pur)
        for _ in range(N):
            drho = (gamma / 2) * (sz @ rho @ sz - rho)
            rho = rho + drho * dt
            rho = rho / np.trace(rho)  # Renormalisation
            
        # Calcul de la pureté
        purity = np.real(np.trace(rho @ rho))
        
        # Calcul de la fidélité
        fid = bures_fidelity_uhlmann(rho, rho_ideal)
        
        # Calcul de l'angle (arccos de la fidélité, pas de la fidélité au carré)
        angle = np.arccos(np.clip(fid, -1.0, 1.0))
        
        results.append((gamma, purity, fid, angle))
        
    return results

if __name__ == "__main__":
    results = run_simulation()
    
    print("Gamma | Pureté | Fidélité Bures | Angle de Bures")
    print("-" * 50)
    for res in results:
        print(f"{res[0]:.3f} | {res[1]:.4f} | {res[2]:.4f} | {res[3]:.4f}")
