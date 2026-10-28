"""
V94 — Forçage unilatéral vs Couplage bidirectionnel (Systèmes lents-rapides)
Compare deux architectures dynamiques :
A) Forçage (beta=0) : l'arrière-plan lent impose sa loi à l'avant-plan rapide.
B) Couplage (beta>0) : l'énergie rapide retroagit sur la dynamique lente.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# 1. PARAMÈTRES GÉNÉRAUX
# ==========================================
fs = 2000          # Fréquence d'échantillonnage pour la simulation
T_total = 10.0     # Durée totale de la simulation (secondes)
t_eval = np.arange(0, T_total, 1/fs)

# Fréquences
f_c = 40.0         # Fréquence rapide (Gamma) - Avant-plan
f_b = 10.0         # Fréquence lente (Alpha) - Arrière-plan
omega_c = 2 * np.pi * f_c
omega_b = 2 * np.pi * f_b

# Échelles de temps
epsilon = 0.05     # Facteur d'échelle pour le temps lent (0 < epsilon << 1)
tau = 0.05         # Constante de temps du filtre passe-bas (q)
q0 = 0.5           # Seuil d'équilibre pour l'énergie rapide
gamma0 = 0.1       # Gain de base de l'oscillateur rapide

# Paramètres de test
beta_unilateral = 0.0  # Cas A : pas de rétroaction
beta_coupled = 2.0     # Cas B : forte rétroaction

# ==========================================
# 2. ÉQUATIONS DIFFÉRENTIELLES
# ==========================================
def system(t, state, beta):
    x, y, q, b = state
    
    # L'arrière-plan b oscille de manière autonome (pour le cas A)
    # ou est influencé par q (pour le cas B)
    b_drive = np.sin(omega_b * t) # Terme de forçage externe (Cas A)
    
    # Fonction de gain (gamma) modulée par l'arrière-plan b
    # On utilise b_drive si beta=0 pour simuler la modulation pure,
    # sinon on utilise la variable dynamique b
    b_eff = b if beta > 0 else b_drive
    
    gamma_b = gamma0 + 0.5 * b_eff
    
    # Oscillateur rapide (Avant-plan)
    dx = -omega_c * y + gamma_b * x
    dy = omega_c * x + gamma_b * y
    
    # Filtre lent de l'énergie (Enveloppe q)
    dq = (x**2 + y**2 - q) / tau
    
    # Dynamique de l'arrière-plan (Arrière-plan)
    # Pour beta=0, b est purement forcé par l'extérieur (on le fixe à b_drive)
    # Pour beta>0, b a sa propre dynamique + rétroaction de q
    if beta == 0:
        db = 0.0 # b est considéré comme fixé par b_drive
    else:
        # Dynamique lente autonome (oscillateur) + rétroaction de l'énergie rapide
        db = epsilon * (-omega_b * 0) + beta * (q - q0) 
        # Note: on pourrait ajouter une vraie oscillation autonome, ici on teste l'effet de la rétroaction
        
    return [dx, dy, dq, db]

# ==========================================
# 3. SIMULATION
# ==========================================
# Conditions initiales : [x, y, q, b]
y0 = [0.1, 0.0, 0.01, 0.0]

print("Simulation du Cas A (Forçage unilatéral)...")
sol_A = solve_ivp(system, [0, T_total], y0, args=(beta_unilateral,), t_eval=t_eval, method='RK45')

print("Simulation du Cas B (Couplage bidirectionnel)...")
sol_B = solve_ivp(system, [0, T_total], y0, args=(beta_coupled,), t_eval=t_eval, method='RK45')

# Extraction des signaux
x_A, q_A, b_A = sol_A.y[0], sol_A.y[2], sol_A.y[3]
x_B, q_B, b_B = sol_B.y[0], sol_B.y[2], sol_B.y[3]

# ==========================================
# 4. ANALYSE SPECTRALE (FFT)
# ==========================================
def compute_fft(signal, fs):
    N = len(signal)
    freqs = np.fft.rfftfreq(N, 1/fs)
    fft_vals = 2.0 * np.abs(np.fft.rfft(signal)) / N
    return freqs, fft_vals

freqs_A, fft_x_A = compute_fft(x_A, fs)
freqs_B, fft_x_B = compute_fft(x_B, fs)

# Zoom sur les basses fréquences pour l'arrière-plan
freqs_q_A, fft_q_A = compute_fft(q_A, fs)
freqs_q_B, fft_q_B = compute_fft(q_B, fs)

# ==========================================
# 5. CRÉATION DES GRAPHIQUES
# ==========================================
fig = plt.figure(figsize=(14, 10))

# Panneau 1 : Signaux temporels (x)
ax1 = plt.subplot(2, 2, 1)
ax1.plot(t_eval[:1000], x_A[:1000], color='blue', alpha=0.7, label='Cas A : Forçage')
ax1.plot(t_eval[:1000], x_B[:1000], color='red', alpha=0.7, label='Cas B : Couplage')
ax1.set_title("Signal Rapide (Avant-plan) - x(t)")
ax1.set_xlabel("Temps (s)")
ax1.set_ylabel("Amplitude")
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

# Panneau 2 : Spectre rapide (Gamma)
ax2 = plt.subplot(2, 2, 2)
mask_gamma = (freqs_A > 30) & (freqs_A < 50)
ax2.plot(freqs_A[mask_gamma], fft_x_A[mask_gamma], color='blue', label='Cas A : Forçage', linestyle='--')
ax2.plot(freqs_B[mask_gamma], fft_x_B[mask_gamma], color='red', label='Cas B : Couplage', alpha=0.7)
ax2.set_title("Spectre Rapide (autour de 40 Hz)")
ax2.set_xlabel("Fréquence (Hz)")
ax2.set_ylabel("Amplitude")
ax2.legend()
ax2.grid(True, alpha=0.3)

# Panneau 3 : Dynamique lente (q)
ax3 = plt.subplot(2, 2, 3)
ax3.plot(t_eval, q_A, color='blue', alpha=0.7, label='Cas A : Forçage')
ax3.plot(t_eval, q_B, color='red', alpha=0.7, label='Cas B : Couplage')
ax3.set_title("Enveloppe Lente Filtrée - q(t)")
ax3.set_xlabel("Temps (s)")
ax3.set_ylabel("Amplitude")
ax3.legend(loc='upper right')
ax3.grid(True, alpha=0.3)

# Panneau 4 : Spectre lent (Alpha / Basses fréquences)
ax4 = plt.subplot(2, 2, 4)
mask_alpha = (freqs_q_A > 0) & (freqs_q_A < 20)
ax4.plot(freqs_q_A[mask_alpha], fft_q_A[mask_alpha], color='blue', label='Cas A : Forçage', linestyle='--')
ax4.plot(freqs_q_B[mask_alpha], fft_q_B[mask_alpha], color='red', label='Cas B : Couplage', alpha=0.7)
ax4.set_title("Spectre Lent (Basses fréquences)")
ax4.set_xlabel("Fréquence (Hz)")
ax4.set_ylabel("Amplitude")
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('v94_forced_vs_coupled.png', dpi=300)
print("Figure sauvegardée : v94_forced_vs_coupled.png")
