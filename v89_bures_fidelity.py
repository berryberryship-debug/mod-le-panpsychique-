import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

# Paramètres
T = 20.0
N = 400
dt = T / N
gammas = [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]

# Matrices de Pauli
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I = np.eye(2, dtype=complex)

# État idéal initial (pur)
rho_ideal = np.array([[1, 0], [0, 0]], dtype=complex)

def bures_fidelity(rho, sigma):
    """Calcule la fidélité de Bures entre deux matrices densité."""
    sqrt_rho = sqrtm(rho)
    inner = sqrtm(sqrt_rho @ sigma @ sqrt_rho)
    return np.real(np.trace(inner)) ** 2

def run_simulation():
    results = []
    
    for gamma in gammas:
        rho = np.copy(rho_ideal)
        
        # Évolution sous l'équation de Lindblad (déphasage pur)
        for _ in range(N):
            # d rho / dt = (gamma / 2) * (sz @ rho @ sz - rho)
            drho = (gamma / 2) * (sz @ rho @ sz - rho)
            rho = rho + drho * dt
            rho = rho / np.trace(rho)  # Renormalisation
            
        # Calcul de la pureté (Plénitude)
        purity = np.real(np.trace(rho @ rho))
        
        # Calcul de la fidélité de Bures (Vacuité)
        fid = bures_fidelity(rho, rho_ideal)
        
        # Angle de Bures
        angle = np.arccos(np.sqrt(fid))
        
        results.append((gamma, purity, fid, angle))
        
    return results

if __name__ == "__main__":
    results = run_simulation()
    
    print("Gamma | Pureté | Fidélité Bures | Angle de Bures")
    print("-" * 50)
    for res in results:
        print(f"{res[0]:.3f} | {res[1]:.4f} | {res[2]:.4f} | {res[3]:.4f}")

    # Génération du graphique (3 panneaux)
    gamma_vals = [r[0] for r in results]
    purity_vals = [r[1] for r in results]
    fidelity_vals = [r[2] for r in results]
    angle_vals = [r[3] for r in results]

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    
    axs[0].plot(gamma_vals, purity_vals, 'o-', color='red')
    axs[0].set_title('Pureté (Plénitude)')
    axs[0].set_xlabel('Gamma')
    
    axs[1].plot(gamma_vals, fidelity_vals, 's-', color='blue')
    axs[1].set_title('Fidélité de Bures (Vacuité)')
    axs[1].set_xlabel('Gamma')
    
    axs[2].plot(gamma_vals, angle_vals, '^-', color='green')
    axs[2].set_title('Angle de Bures')
    axs[2].set_xlabel('Gamma')
    
    plt.tight_layout()
    plt.savefig('v89_bures_fidelity.png')
    print("\nFigure sauvegardée : v89_bures_fidelity.png")
