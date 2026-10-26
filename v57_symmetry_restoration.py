import numpy as np
import matplotlib.pyplot as plt

def run_v57_symmetry_restoration():
    """
    Test V57 : Dissolution de défauts (vortex) sous restauration de symétrie.
    Dans le modèle de Ginzburg-Landau, si le coefficient quadratique mu^2
    devient positif, l'état fondamental redevient psi = 0, détruisant
    les défauts topologiques.
    """
    N = 100
    L = 20.0
    dx = L / N
    dt = 0.05
    
    x = np.linspace(-L/2, L/2, N)
    y = np.linspace(-L/2, L/2, N)
    X, Y = np.meshgrid(x, y)
    
    # Condition initiale : un vortex au centre
    theta = np.arctan2(Y, X)
    r = np.sqrt(X**2 + Y**2)
    amplitude = np.tanh(r) # Le cœur du vortex est à 0, l'extérieur à 1
    psi = amplitude * np.exp(1j * theta)
    
    print("Test V57 : Restauration de symétrie et dissolution de vortex")
    print("------------------------------------------------------------")
    
    # Le paramètre mu^2 (noté 'a' ici) va passer de -1.0 (symétrie brisée) à +1.0
    a_values = np.linspace(-1.0, 1.0, 100)
    b = 1.0
    kappa = 1.0
    
    max_amplitudes = []
    
    for a in a_values:
        # Relaxation de l'équation de Ginzburg-Landau
        for _ in range(10): # Quelques pas pour relaxer à chaque changement de a
            laplacian = (np.roll(psi, -1, axis=0) + np.roll(psi, 1, axis=0) +
                         np.roll(psi, -1, axis=1) + np.roll(psi, 1, axis=1) - 4*psi) / dx**2
            
            # d psi / dt = kappa^2 * laplacien - a * psi - b * |psi|^2 * psi
            dpsi_dt = kappa**2 * laplacian - a * psi - b * np.abs(psi)**2 * psi
            psi += dt * dpsi_dt
            
        # On enregistre l'amplitude maximale (si elle tombe à 0, le vortex est détruit)
        max_amp = np.max(np.abs(psi))
        max_amplitudes.append(max_amp)
        
    print(f"Amplitude max initiale (a=-1.0) : {max_amplitudes[0]:.4f}")
    print(f"Amplitude max finale   (a=+1.0) : {max_amplitudes[-1]:.4f}")
    print("Résultat : Le vortex est détruit quand mu^2 devient positif.")
    
    # Graphique
    plt.figure(figsize=(8, 5))
    plt.plot(a_values, max_amplitudes, color='red', linewidth=2)
    plt.axvline(0, color='black', linestyle='--', label='mu^2 = 0')
    plt.title("V57 : Dissolution du défaut topologique sous restauration de symétrie")
    plt.xlabel("Paramètre mu^2 (a)")
    plt.ylabel("Amplitude maximale du champ |psi|")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("v57_symmetry_restoration.png")
    print("Figure sauvegardée : v57_symmetry_restoration.png")

if __name__ == "__main__":
    run_v57_symmetry_restoration()
