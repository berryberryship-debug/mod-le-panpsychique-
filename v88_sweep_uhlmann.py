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
        commutator = -1j * (H @ rho - rho @ H)
        dephasing = (gamma / 2.0) * (sigma_z @ rho @ sigma_z - rho)
        
        rho += dt * (commutator + dephasing)
        rho /= np.trace(rho)

        trace_val = np.real(np.trace(sqrtm(rho)))
        traces.append(trace_val)

    return np.array(traces)

if __name__ == "__main__":
    print("Test V88 : Balayage fin de Gamma (Effondrement de la phase d'Uhlmann)")
    print("---------------------------------------------------------------------")
    
    # Balayage fin de gamma
    gamma_sweep = np.linspace(0.0, 0.5, 20)
    final_traces = []
    
    for gamma in gamma_sweep:
        trace_vals = compute_uhlmann_trace(gamma)
        final_traces.append(trace_vals[-1]) # On garde la valeur finale
        
    final_traces = np.array(final_traces)
    
    # Sauvegarde des données brutes
    np.savez("v88_sweep_data.npz", gamma=gamma_sweep, final_traces=final_traces)
    print("Données sauvegardées : v88_sweep_data.npz")

    # Génération de la figure à 3 panneaux
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    
    # Panneau 1 : Trace finale en fonction de gamma
    axs[0].plot(gamma_sweep, final_traces, 'o-', color='purple')
    axs[0].set_title("Trace finale vs Gamma")
    axs[0].set_xlabel("Gamma")
    axs[0].set_ylabel("|Tr| finale")
    
    # Panneau 2 : Dérivée (taux de changement)
    deriv = np.gradient(final_traces, gamma_sweep)
    axs[1].plot(gamma_sweep, deriv, 's-', color='orange')
    axs[1].set_title("Dérivée (Taux d'effondrement)")
    axs[1].set_xlabel("Gamma")
    axs[1].set_ylabel("d|Tr|/dGamma")
    
    # Panneau 3 : Asymptote mathématique
    axs[2].axhline(1/np.sqrt(2), color='red', linestyle='--', label='1/√2 (asymptote)')
    axs[2].plot(gamma_sweep, final_traces, '^-', color='blue', alpha=0.5)
    axs[2].set_title("Comparaison avec l'asymptote")
    axs[2].set_xlabel("Gamma")
    axs[2].legend()
    
    plt.tight_layout()
    plt.savefig("v88_sweep_uhlmann.png")
    print("Figure sauvegardée : v88_sweep_uhlmann.png")
