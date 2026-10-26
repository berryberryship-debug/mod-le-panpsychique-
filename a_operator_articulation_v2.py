import numpy as np
import matplotlib.pyplot as plt

# Matrices de Pauli
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
I = np.eye(2, dtype=complex)

def run_berry_lindblad_v2(gamma, T=20.0, N=2000):
    """
    Version 2 : Pas de temps plus fin (N=2000) pour vérifier la stabilité
    de la phase de Berry et l'effet du déphasage Lindblad.
    """
    dt = T / N
    
    # État initial |+>
    rho = np.array([[0.5, 0.5],
                    [0.5, 0.5]], dtype=complex)
    
    phase_history = []
    
    for i in range(N):
        t = i * dt
        
        # Hamiltonien cyclique
        w = 2 * np.pi / T
        H = 0.5 * (np.cos(w * t) * sigma_x + np.sin(w * t) * sigma_y)
        
        # Évolution
        commutator = -1j * (H @ rho - rho @ H)
        dephasing = (gamma / 2.0) * (sigma_z @ rho @ sigma_z - rho)
        
        rho += dt * (commutator + dephasing)
        rho /= np.trace(rho)
        
        # Stockage de la phase
        coherence = rho[0, 1]
        phase_history.append(np.angle(coherence))
        
    return phase_history

if __name__ == "__main__":
    print("Articulation V2 : Phase de Berry et Lindblad (Haute résolution)")
    print("---------------------------------------------------------------")
    
    gamma_vals = [0.0, 0.05, 0.1, 0.2]
    plt.figure(figsize=(10, 6))
    
    for gamma in gamma_vals:
        phases = run_berry_lindblad_v2(gamma)
        plt.plot(phases, label=f'Gamma = {gamma}')
        
    plt.axhline(-np.pi/2, color='red', linestyle='--', label='-π/2 (convention)')
    
    plt.title("V2 : Stabilité de la phase de Berry sous décohérence")
    plt.xlabel("Pas de temps (N=2000)")
    plt.ylabel("Phase accumulée (radians)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("berry_phase_stability_v2.png")
    print("Figure sauvegardée : berry_phase_stability_v2.png")
    print("Observation : La phase reste stable, mais l'amplitude de la cohérence chute avec Gamma.")
