"""
V93 — Modulation d'amplitude et bandes latérales

Une porteuse sinusoïdale à 40 Hz est modulée par une
enveloppe sinusoïdale à 10 Hz.

Le script compare le spectre idéal au spectre bruité et
illustre les bandes latérales à 30 et 50 Hz.

Statut : démonstration mathématique. La modulation est
imposée par construction ; aucun couplage neuronal n'est estimé.
"""

import numpy as np
import matplotlib.pyplot as plt

# Graine aléatoire pour la reproductibilité
np.random.seed(42)

# ==========================================
# 1. GÉNÉRATION DES SIGNAUX
# ==========================================
fs = 1000 
T = 1.0 # 1 seconde
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Signal visuel réel (Gamma 40 Hz)
f_visuel = 40
signal_visuel = np.sin(2 * np.pi * f_visuel * t) + 0.1 * np.random.randn(len(t))

# Signal de contexte/anticipation (Alpha 10 Hz)
f_alpha = 10
signal_alpha = np.sin(2 * np.pi * f_alpha * t)

# ==========================================
# 2. MODULATION D'AMPLITUDE
# ==========================================
# Modulation imposée : analogue mathématique d'un PAC,
# sans estimation de couplage neuronal ni modèle inhibiteur.
signal_module = signal_visuel * (1 + 0.5 * signal_alpha)

# Signal idéal sans bruit (pour comparaison spectrale)
signal_ideal = np.sin(2 * np.pi * f_visuel * t) * (1 + 0.5 * np.sin(2 * np.pi * f_alpha * t))

# ==========================================
# 3. ANALYSE SPECTRALE (FFT)
# ==========================================
def spectre(x):
    # Normalisation : amplitude réelle d'une sinusoïde = 1
    f = np.fft.rfftfreq(len(x), 1/fs)
    a = 2 * np.abs(np.fft.rfft(x)) / len(x)
    return f, a

f, a_bruit = spectre(signal_module)
_, a_ideal = spectre(signal_ideal)
m = f < 60

# ==========================================
# 4. CRÉATION DES GRAPHIQUES (4 panneaux)
# ==========================================
fig, axs = plt.subplots(4, 1, figsize=(12, 12))

# Graphique 1 : Le signal visuel brut
axs[0].plot(t[:200], signal_visuel[:200], color='red', alpha=0.7)
axs[0].set_title(
    "1. Porteuse sensorielle simulée (40 Hz)"
)
axs[0].set_ylabel("Amplitude")
axs[0].grid(True, alpha=0.3)

# Graphique 2 : L'onde alpha (contexte)
axs[1].plot(t[:200], signal_alpha[:200], color='purple', linewidth=3)
axs[1].set_title(
    "2. Enveloppe de modulation (10 Hz)"
)
axs[1].set_ylabel("Amplitude")
axs[1].grid(True, alpha=0.3)

# Graphique 3 : Le signal modulé dans le temps
axs[2].plot(t[:200], signal_module[:200], color='blue', alpha=0.8, label='Signal Modulé (avec bruit)')
axs[2].plot(t[:200], signal_visuel[:200], color='red', linestyle='--', alpha=0.4, label='Réel pur')
axs[2].set_title(
    "3. Signal modulé : comparaison temporelle"
)
axs[2].set_ylabel("Amplitude")
axs[2].legend(loc='upper right')
axs[2].grid(True, alpha=0.3)

# Graphique 4 : Le spectre (L'identité mathématique)
axs[3].plot(f[m], a_bruit[m], color="black", label="Avec bruit")
axs[3].plot(f[m], a_ideal[m], color="orange", linestyle=":", label="Idéal (sans bruit)")
axs[3].set_title("4. Spectre : identité mathématique de la modulation d'amplitude")
axs[3].set_xlabel("Fréquence (Hz)")
axs[3].set_ylabel("Amplitude (normalisée)")

ymax = axs[3].get_ylim()[1]
for freq, label in [(30, "30 Hz : bande latérale"),
                    (40, "40 Hz : porteuse"),
                    (50, "50 Hz : bande latérale")]:
    axs[3].axvline(freq, color="gray", linestyle="--", alpha=0.7)
    axs[3].text(freq + 0.5, 0.95 * ymax, label, rotation=90, va="top", fontsize=8)

axs[3].legend(loc="upper left")
axs[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('v93_modulation_amplitude.png', dpi=300)
print("Figure sauvegardée : v93_modulation_amplitude.png")
