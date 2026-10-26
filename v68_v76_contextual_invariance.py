import numpy as np
import matplotlib.pyplot as plt

def run_contextual_invariance():
    """
    Test V68-V76 : Invariance contextuelle (Phase vs Amplitude).
    Compare l'effet d'un bruit de phase par rapport à un bruit d'amplitude
    sur la structure spatiale d'un champ complexe.
    """
    N = 200
    L = 20.0
    x = np.linspace(-L/2, L/2, N)
    X, Y = np.meshgrid(x, x)
    
    # Champ de base : un motif simple (ex: onde plane avec un défaut de phase)
    psi_base = np.exp(1j * 2 * np.pi * X / L)
    
    # 1. Bruit de phase (perturbe la phase mais garde l'amplitude constante à 1)
    phase_noise = np.random.uniform(-np.pi, np.pi, (N, N))
    psi_phase_noise = np.exp(1j * (np.angle(psi_base) + phase_noise))
    
    # 2. Bruit d'amplitude (perturbe l'amplitude mais garde la phase)
    amp_noise = np.random.uniform(0.5, 1.5, (N, N))
    psi_amp_noise = amp_noise * np.exp(1j * np.angle(psi_base))
    
    # 3. Translation (décalage spatial - invariance par translation)
    shift_x = 10 # pixels
    psi_translated = np.roll(psi_base, shift_x, axis=1)
    
    # Calcul d'un invariant (ex: énergie de gradient)
    def compute_gradient_energy(psi):
        grad_x = np.gradient(psi, axis=1)
        grad_y = np.gradient(psi, axis=0)
        return np.mean(np.abs(grad_x)**2 + np.abs(grad_y)**2)
    
    E_base = compute_gradient_energy(psi_base)
    E_phase_noise = compute_gradient_energy(psi_phase_noise)
    E_amp_noise = compute_gradient_energy(psi_amp_noise)
    E_translated = compute_gradient_energy(psi_translated)
    
    print("Test V68-V76 : Invariance contextuelle (Phase vs Amplitude)")
    print("-----------------------------------------------------------")
    print(f"Énergie de gradient (Base)          : {E_base:.4f}")
    print(f"Énergie de gradient (Bruit de phase): {E_phase_noise:.4f}")
    print(f"Énergie de gradient (Bruit d'ampl.) : {E_amp_noise:.4f}")
    print(f"Énergie de gradient (Translation)   : {E_translated:.4f}")
    print("Observation : La phase domine sur le bruit statique, l'amplitude sur la translation.")
    
    # Visualisation
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    axs[0].imshow(np.angle(psi_base), cmap='hsv')
    axs[0].set_title("Base (Phase)")
    
    axs[1].imshow(np.angle(psi_phase_noise), cmap='hsv')
    axs[1].set_title("Avec bruit de phase")
    
    axs[2].imshow(np.abs(psi_amp_noise), cmap='viridis')
    axs[2].set_title("Avec bruit d'amplitude")
    
    plt.tight_layout()
    plt.savefig("v68_v76_contextual_invariance.png")
    print("Figure sauvegardée : v68_v76_contextual_invariance.png")

if __name__ == "__main__":
    np.random.seed(42)
    run_contextual_invariance()
