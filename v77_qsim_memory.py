import numpy as np
import matplotlib.pyplot as plt

# Matrices de Pauli
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

def run_v77_markov():
    # Paramètres
    gamma = 0.1  # Taux de déphasage
    T = 20.0     # Temps total
    N = 400      # Nombre de pas
    dt = T / N

    # Condition initiale : état pur |+> (superposition)
    rho = np.array([[0.5, 0.5],
                    [0.5, 0.5]], dtype=complex)

    purities = []

    # Évolution de Lindblad (déphasage markovien)
    for _ in range(N):
        # d rho / dt = (gamma / 2) * (sigma_z @ rho @ sigma_z - rho)
        drho = (gamma / 2) * (sigma_z @ rho @ sigma_z - rho)
        rho = rho + drho * dt
        # Assurer la trace = 1
        rho = rho / np.trace(rho)

        # Calcul de la pureté Tr(rho^2)
        purity = np.real(np.trace(rho @ rho))
        purities.append(purity)

    return purities

if __name__ == "__main__":
    purities = run_v77_markov()
    
    print("Test V77 : Décohérence markovienne")
    print("---------------------------------")
    print(f"Pureté finale : {purities[-1]:.4f}")
    print("Valeur asymptotique attendue (mélange maximal) : 0.5000")

    # Génération de la figure
    plt.figure(figsize=(8, 5))
    plt.plot(purities, label='Pureté simulée', color='blue')
    plt.axhline(0.5, color='red', linestyle='--', label='Mélange maximal (0.5)')
    plt.title("V77 : Décohérence markovienne (chute de la pureté)")
    plt.xlabel("Pas de temps")
    plt.ylabel("Pureté Tr(rho^2)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("v77_purity_decay.png")
    print("Figure sauvegardée : v77_purity_decay.png")
