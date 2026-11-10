import numpy as np
import matplotlib.pyplot as plt

sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

def run_v78_nonmarkov_fixed():
    T = 20.0     
    N = 1000     
    dt = T / N
    time = np.linspace(0, T, N)

    # CORRECTION 1 : État initial en superposition (|+>)
    rho = np.array([[0.5, 0.5],
                    [0.5, 0.5]], dtype=complex)

    purities = []

    for t in time:
        # CORRECTION 2 : Taux qui devient négatif (signature non-markovienne)
        gamma_t = 0.5 * (1 - 1.5 * np.sin(5 * t)) 
        
        drho = (gamma_t / 2) * (sigma_z @ rho @ sigma_z - rho)
        rho = rho + drho * dt
        rho = rho / np.trace(rho)

        purity = np.real(np.trace(rho @ rho))
        purities.append(purity)

    return time, purities

if __name__ == "__main__":
    time, purities = run_v78_nonmarkov_fixed()
    print("Test V78 (Corrigé) : Mémoire non-markovienne")
    print(f"Pureté minimale atteinte : {min(purities):.4f}")
    print(f"Pureté finale : {purities[-1]:.4f}")
    
    plt.figure(figsize=(8, 5))
    plt.plot(time, purities, color='purple', label='Pureté (non-markovien corrigé)')
    plt.title("V78 : Récurrences quantiques (vraies)")
    plt.xlabel("Temps")
    plt.ylabel("Pureté")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("v78_nonmarkov_fixed.png")
    print("Figure sauvegardée.")
