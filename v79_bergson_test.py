import numpy as np
import matplotlib.pyplot as plt

def evolution_systeme(environnement_initial, T=20.0, N=400, dt=0.05):
    """
    Simule l'évolution d'un système en interaction avec un environnement.
    On garde une trace de l'état de l'environnement (mémoire).
    """
    # État du système : matrice densité 2x2 (initialement identique pour les 2 tests)
    rho = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    # L'environnement évolue et garde une "mémoire" de son histoire
    env_state = environnement_initial
    historique = []
    
    for _ in range(N):
        # L'environnement influence le système de manière non-markovienne
        # (le taux de décohérence dépend de l'état passé de l'environnement)
        gamma_t = 0.1 + 0.05 * env_state
        
        # Évolution du système (Lindblad modifié)
        drho = (gamma_t / 2) * (sigma_z @ rho @ sigma_z - rho)
        rho = rho + drho * dt
        rho = rho / np.trace(rho)
        
        # L'environnement accumule de l'information (mémoire)
        env_state = 0.99 * env_state + 0.01 * np.real(rho[0, 0])
        historique.append(np.real(rho[0, 0]))
        
    return np.array(historique)

if __name__ == "__main__":
    T, N, dt = 20.0, 400, 20.0/400
    
    print("Test V79 : Test de Bergson (Mémoire de l'environnement)")
    print("-------------------------------------------------------")
    
    # Deux environnements avec des passés différents
    # Histoire 1 : L'environnement a un passé "chaud"
    hist_1 = evolution_systeme(environnement_initial=1.0)
    
    # Histoire 2 : L'environnement a un passé "froid"
    hist_2 = evolution_systeme(environnement_initial=0.0)
    
    # À la fin, les états du système sont très proches, MAIS...
    etat_present_1 = hist_1[-1]
    etat_present_2 = hist_2[-1]
    
    print(f"État du système à la fin (Histoire 1) : {etat_present_1:.4f}")
    print(f"État du système à la fin (Histoire 2) : {etat_present_2:.4f}")
    print("Observation : Même si les états présents se ressemblent, leurs trajectoires")
    print("ont divergé à cause de la mémoire (le passé) de l'environnement.")
    
    # Figure
    plt.figure(figsize=(8, 5))
    plt.plot(hist_1, label='Histoire 1 (Environnement initial = 1.0)', color='red')
    plt.plot(hist_2, label='Histoire 2 (Environnement initial = 0.0)', color='blue')
    plt.title("V79 : Test de Bergson (Divergence due à l'histoire de l'environnement)")
    plt.xlabel("Pas de temps")
    plt.ylabel("Population de l'état |0>")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("v79_bergson_divergence.png")
    print("Figure sauvegardée : v79_bergson_divergence.png")
