import numpy as np

# Opérateurs de Pauli
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

# 1. Pré-sélection (Le passé, l'état initial : |0>)
psi_initial = np.array([1, 0], dtype=complex)

# 2. Post-sélection (Le futur, l'état final : |1>)
phi_final = np.array([0, 1], dtype=complex)

# 3. Hamiltonien d'interaction (ex: champ magnétique qui fait tourner l'état)
# H = (pi/2) * sx  (Rotation d'un quart de tour)
H = (np.pi / 2) * sx

# Opérateur d'évolution U(t) = exp(-i H t)
# Ici on choisit un temps t pour que l'état initial devienne presque orthogonal à l'état final
t = 0.99  # Proche de 1, juste avant que l'amplitude de transition ne s'annule
from scipy.linalg import expm
U = expm(-1j * H * t)

# L'état qui a évolué depuis le passé
psi_t = U @ psi_initial

# L'opérateur à mesurer (A = sx)
A = sx

# --- CALCUL DE LA VALEUR FAIBLE (Weak Value) ---
# A_w = <phi| A |psi_t> / <phi| psi_t>
amplitude_transition = np.vdot(phi_final, psi_t) # <phi|psi_t>
valeur_faible = np.vdot(phi_final, A @ psi_t) / amplitude_transition

print("--- Formalisme à deux vecteurs (TSVF) ---")
print(f"Amplitude de transition <phi|psi> : {amplitude_transition:.4f}")
print(f"Valeur Faible (Weak Value) A_w    : {valeur_faible:.4f}")

# Si la probabilité de transition est très faible, la valeur faible peut être
# très grande et même sortir de l'intervalle classique des valeurs propres (-1 à 1).

# --- RECONFIGURATION DE LA MATRICE DENSITÉ ---
# Matrice densité standard (sans regarder le futur)
rho_standard = np.outer(psi_t, psi_t.conj())

# Matrice densité post-sélectionnée (rétrocausalité)
# On projette l'état présent sur l'état futur
projeteur_futur = np.outer(phi_final, phi_final.conj())
rho_postsel = projeteur_futur @ rho_standard @ projeteur_futur
# On renormalise par la probabilité de transition
if np.abs(amplitude_transition) > 1e-10:
    rho_postsel = rho_postsel / (np.abs(amplitude_transition)**2)

print(f"\nPureté standard Tr(rho^2)         : {np.real(np.trace(rho_standard @ rho_standard)):.4f}")
print(f"Pureté post-sélectionnée          : {np.real(np.trace(rho_postsel @ rho_postsel)):.4f}")
