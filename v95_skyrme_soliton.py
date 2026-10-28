"""
V95 — Soliton de Skyrme (Ansatz Hedgehog)
Résolution de l'équation du profil radial F(r) pour un skyrmion de charge B=1.
Illustre comment une topologie globale (Vacuité) stabilise une configuration
locale (Plénitude).
"""

import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

# ==========================================
# 1. ÉQUATION DIFFÉRENTIELLE DE SKYRME
# ==========================================
def skyrme_ode(r, y):
    """
    y[0] = F(r)
    y[1] = F'(r)
    Équation : (r^2 + 2sin^2 F)F'' + 2rF' + sin(2F)[(F')^2 - 1 - sin^2(F)/r^2] = 0
    """
    F = y[0]
    dF = y[1]
    
    # Éviter la division par zéro en r=0 (on commence à r=1e-5)
    sin2F = np.sin(2 * F)
    sin2F_val = np.sin(F)**2
    
    # Isoler F''
    num = -2 * r * dF - sin2F * (dF**2 - 1 - sin2F_val / r**2)
    den = r**2 + 2 * sin2F_val
    d2F = num / den
    
    return np.vstack((dF, d2F))

def bc(ya, yb):
    """
    Conditions aux limites :
    En r=0 (ya) : F = pi
    En r=inf (yb) : F = 0
    """
    return np.array([ya[0] - np.pi, yb[0] - 0.0])

# ==========================================
# 2. RÉSOLUTION NUMÉRIQUE
# ==========================================
# Grille spatiale (éviter r=0 exactement)
r = np.linspace(1e-5, 15.0, 500)

# Estimation initiale (guess) : une fonction qui descend de pi à 0
# On utilise une tangente hyperbolique pour lisser la transition
F_guess = np.pi * 0.5 * (1 - np.tanh(r - 2.0))
dF_guess = np.gradient(F_guess, r)
y_guess = np.vstack((F_guess, dF_guess))

print("Résolution de l'équation de Skyrme (B=1)...")
sol = solve_bvp(skyrme_ode, bc, r, y_guess, tol=1e-6, max_nodes=2000)

if not sol.success:
    raise RuntimeError("Échec de la convergence du solveur BVP.")

F_sol = sol.sol(r)[0]
dF_sol = sol.sol(r)[1]

# ==========================================
# 3. CALCUL DE LA CHARGE TOPOLOGIQUE (B)
# ==========================================
# B = (F(0) - F(inf)) / pi
B = (F_sol[0] - F_sol[-1]) / np.pi
print(f"Charge topologique calculée : B = {B:.4f}")

# ==========================================
# 4. DENSITÉ D'ÉNERGIE (simplifiée pour visualisation)
# ==========================================
# La densité d'énergie dépend de F' et sin(F)/r
# On calcule une version adimensionnelle pour voir la localisation (Plénitude)
energy_density = (dF_sol**2 + 2 * np.sin(F_sol)**2 / r**2) * r**2

# ==========================================
# 5. GRAPHIQUES
# ==========================================
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Panneau 1 : Profil F(r)
axs[0].plot(r, F_sol, color='blue', linewidth=2)
axs[0].axhline(np.pi, color='red', linestyle='--', label='F(0) = π')
axs[0].axhline(0, color='green', linestyle='--', label='F(∞) = 0')
axs[0].set_title("Profil radial F(r)")
axs[0].set_xlabel("r")
axs[0].set_ylabel("F(r)")
axs[0].legend()
axs[0].grid(True, alpha=0.3)

# Panneau 2 : Dérivée F'(r)
axs[1].plot(r, dF_sol, color='purple', linewidth=2)
axs[1].set_title("Dérivée F'(r)")
axs[1].set_xlabel("r")
axs[1].set_ylabel("F'(r)")
axs[1].grid(True, alpha=0.3)

# Panneau 3 : Densité d'énergie (Plénitude locale)
axs[2].plot(r, energy_density, color='orange', linewidth=2)
axs[2].fill_between(r, energy_density, alpha=0.3, color='orange')
axs[2].set_title("Densité d'énergie locale")
axs[2].set_xlabel("r")
axs[2].set_ylabel("Densité")
axs[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('v95_skyrme_soliton.png', dpi=300)
print("Figure sauvegardée : v95_skyrme_soliton.png")
