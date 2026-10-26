import numpy as np

def generer_sequence(N=1000, dt=0.01, bruit_std=0.1):
    """Génère une séquence temporelle issue d'une dynamique classique linéaire."""
    x = np.zeros(N)
    x[0] = 1.0  # Condition initiale
    
    # Dynamique linéaire markovienne (AR(1)) : x(t+1) = a * x(t) + bruit
    a = 0.95
    for t in range(1, N):
        x[t] = a * x[t-1] + np.random.normal(0, bruit_std)
    return x

def test_permutation_memoire(x, n_permutations=1000):
    """
    Test de permutation pour détecter une mémoire historique.
    Si la dynamique est purement markovienne, permuter l'ordre temporel
    ne devrait pas changer la distribution statistique de la série.
    """
    # Statistique observée (ex: autocorrélation à un certain lag)
    lag = 5
    obs_stat = np.corrcoef(x[:-lag], x[lag:])[0, 1]
    
    # Statistiques sous permutations (mélange de l'ordre temporel)
    perm_stats = []
    for _ in range(n_permutations):
        x_perm = np.random.permutation(x)
        perm_stat = np.corrcoef(x_perm[:-lag], x_perm[lag:])[0, 1]
        perm_stats.append(perm_stat)
        
    perm_stats = np.array(perm_stats)
    
    # Calcul de la p-valeur (test bilatéral)
    p_value = np.mean(np.abs(perm_stats) >= np.abs(obs_stat))
    
    return obs_stat, p_value

if __name__ == "__main__":
    np.random.seed(42)
    
    print("Test V82 : Mémoire historique dans une dynamique classique")
    print("----------------------------------------------------------")
    
    # 1. Générer la série temporelle
    serie = generer_sequence()
    
    # 2. Appliquer le test de permutation
    obs_stat, p_value = test_permutation_memoire(serie)
    
    print(f"Statistique observée (autocorrélation lag=5) : {obs_stat:.4f}")
    print(f"p-valeur (test de permutation) : {p_value:.4f}")
    
    # Conclusion basée sur le seuil standard de 0.05
    if p_value < 0.05:
        print("Résultat : Rejet de H0. Mémoire historique détectée.")
    else:
        print("Résultat : Négatif propre. Pas de mémoire historique dans cette dynamique linéaire.")
