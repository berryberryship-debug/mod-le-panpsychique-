import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

# Matrices de Pauli
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)

def compute_uhlmann_trace(gamma, T=10.0, N=500):
    dt = T / N
    rho = np.array([[1, 0], [0, 0]], dtype=complex) # État initial pur
    H = (sigma_x / 2.0) # Hamiltonien cyclique

    traces = []
    for _ in range(N):
        # Évolution de Lindblad : -i[H, rho] + (gamma/2)(sigma_z rho sigma_z - rho)
        commutator = -1j * (H @ rho - rho @ H)
        dephasing = (gamma / 2.0) * (sigma_z @ rho @ sigma_z - rho)
        
        rho += dt * (commutator + dephasing)
        rho /= np.trace(rho)  # Renormalisation

        # Calcul de la trace (approximation de la racine pour la phase d'Uhlmann)
        trace_val = np.real(np.trace(sqrtm(rho)))
        traces.append(trace_val)

    return np.array(traces)

if __name__ == "__main__":
    print("Test V86 : Phase d'Uhlmann (convergence et instabilité)")
    print("-------------------------------------------------------")
    
    gamma_vals = [0.01, 0.025, 0.05]
    plt.figure(figsize=(8, 5))
    
    for gamma in gamma_vals:
        trace_vals = compute_uhlmann_trace(gamma)
        plt.plot(trace_vals, label=f'Gamma = {gamma}')

    plt.title("V86 : Trace de la racine de la matrice densité")
    plt.xlabel("Pas de temps")
    plt.ylabel("|Tr|")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("v86_uhlmann_phase.png")
    print("Figure sauvegardée : v86_uhlmann_phase.png")
    print("Note : Instabilité numérique attendue autour de gamma = 0.025.")
