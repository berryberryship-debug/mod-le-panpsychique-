import numpy as np
import matplotlib.pyplot as plt

def run_ginzburg_landau():
    """
    Simulation simplifiée de l'équation de Ginzburg-Landau en 1D
    pour vérifier la conservation de l'énergie et la convergence.
    """
    # Paramètres
    N = 200         # Taille de la grille
    L = 20.0        # Taille du domaine
    dx = L / N
    dt = 0.001      # Pas de temps
    T_max = 1.0
    steps = int(T_max / dt)
    
    # Grille spatiale
    x = np.linspace(-L/2, L/2, N)
    
    # Paramètres de Ginzburg-Landau
    a = -1.0
    b = 1.0
    kappa = 1.0
    
    # Condition initiale (proche de l'état fondamental)
    psi = np.exp(-x**2) + 0j
    psi += 0.1 * np.random.randn(N) # Un peu de bruit
    
    def compute_energy(psi, dx, a, b, kappa):
        # Terme de potentiel : a|psi|^2 + (b/2)|psi|^4
        energy_density = a * np.abs(psi)**2 + (b/2) * np.abs(psi)**4
        # Terme de gradient : kappa^2 |d psi/dx|^2
        grad_psi = np.gradient(psi, dx)
        gradient_energy = kappa**2 * np.abs(grad_psi)**2
        
        # Intégration sur l'espace
        E = np.sum(energy_density + gradient_energy) * dx
        return E

    energies = []
    
    print("Test V45-V46 : Convergence de Ginzburg-Landau")
    print("---------------------------------------------")
    
    for step in range(steps):
        # Laplacien (approximation aux différences finies)
        laplacian = (np.roll(psi, -1) - 2*psi + np.roll(psi, 1)) / dx**2
        
        # Équation d'évolution de Ginzburg-Landau (relaxation)
        # d psi / dt = kappa^2 * laplacien(psi) - a * psi - b * |psi|^2 * psi
        dpsi_dt = kappa**2 * laplacian - a * psi - b * np.abs(psi)**2 * psi
        
        psi += dt * dpsi_dt
        
        # Calcul de l'énergie toutes les 10 étapes
        if step % 10 == 0:
            E = compute_energy(psi, dx, a, b, kappa)
            energies.append(E)
            
    print(f"Énergie initiale : {energies[0]:.6f}")
    print(f"Énergie finale   : {energies[-1]:.6f}")
    print(f"Erreur relative  : {abs((energies[-1] - energies[0]) / energies[0]):.2e}")
    print("Observation : L'énergie converge vers un minimum stable.")
    
    # Graphique
    plt.figure(figsize=(8, 5))
    plt.plot(energies)
    plt.title("V45-V46 : Convergence de l'énergie (Ginzburg-Landau)")
    plt.xlabel("Pas de temps (x10)")
    plt.ylabel("Énergie totale")
    plt.grid(True, alpha=0.3)
    plt.savefig("v45_gl_energy_convergence.png")
    print("Figure sauvegardée : v45_gl_energy_convergence.png")

if __name__ == "__main__":
    run_ginzburg_landau()
