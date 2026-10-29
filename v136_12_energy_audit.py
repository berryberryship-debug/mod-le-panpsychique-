"""
V136.12 — Bilan énergétique (Assertions Dynamiques).
Vérifie la conservation de l'énergie et de la norme pour le modèle A (fermé).
"""
import numpy as np
from scipy.integrate import solve_ivp

# Paramètres
N = 50
t_hop = 1.0
U = 1.0
WX, WZ = 0.5, 1.0
j0 = N // 2
NPART = 10.0
phi = 0.5

def build_hamiltonian(phi):
    H = np.zeros((N, N), dtype=complex)
    phase = 2 * np.pi * phi / N
    for j in range(N):
        j_next = (j + 1) % N
        H[j, j_next] = -t_hop * np.exp(1j * phase)
        H[j_next, j] = -t_hop * np.exp(-1j * phase)
    return H

def simulate_ferme(g_coupl, T=50.0, dt=0.05, rtol=1e-10, atol=1e-12):
    """Modèle A (rétroaction bidirectionnelle, fermé)."""
    H = build_hamiltonian(phi)
    x = np.arange(N)
    psi0 = np.exp(-0.05 * (x - j0)**2).astype(complex)
    psi0 *= np.sqrt(NPART / np.sum(np.abs(psi0)**2))
    r0 = np.array([0.0, 0.0, 1.0])
    y0 = np.concatenate([psi0.real, psi0.imag, r0])
    te = np.linspace(0.0, T, int(round(T / dt)) + 1)

    def rhs(t, y):
        psi = y[:N] + 1j * y[N:2*N]
        r = y[2*N:]
        rho_j0 = np.abs(psi[j0])**2
        
        H_psi = H @ psi
        H_psi += U * np.abs(psi)**2 * psi
        if g_coupl > 0:
            H_psi[j0] += g_coupl * r[2] * psi[j0]
            
        dpsi = -1j * H_psi
        Omega = np.array([WX, 0.0, WZ + 2 * g_coupl * rho_j0])
        dr = np.cross(Omega, r)
        return np.concatenate([dpsi.real, dpsi.imag, dr])

    sol = solve_ivp(rhs, (0, T), y0, t_eval=te, method="DOP853", rtol=rtol, atol=atol)
    if not sol.success:
        raise RuntimeError(f"Échec solve_ivp : {sol.message}")
        
    psi = sol.y[:N] + 1j * sol.y[N:2*N]
    r = sol.y[2*N:]
    
    # Énergies
    phase = 2 * np.pi * phi / N
    E_kin = np.zeros_like(te)
    for j in range(N):
        j_next = (j + 1) % N
        E_kin += -2.0 * t_hop * np.real(np.conj(psi[j]) * np.exp(1j*phase) * psi[j_next])
    
    E_pot = 0.5 * U * np.sum(np.abs(psi)**4, axis=0)
    E_q = 0.5 * (WX * r[0] + WZ * r[2])
    E_int = g_coupl * np.abs(psi[j0])**2 * r[2] if g_coupl > 0 else np.zeros_like(te)
    E_tot = E_kin + E_pot + E_q + E_int
    
    # Norme
    norme = np.sum(np.abs(psi)**2, axis=0)
    
    return dict(t=te, E_tot=E_tot, norme=norme)

if __name__ == "__main__":
    print("=== V136.12 : Bilan énergétique (Assertions Dynamiques) ===")
    
    s = simulate_ferme(g_coupl=1.0)
    
    # Calcul des dérives
    derive_E = np.max(np.abs(s["E_tot"] - s["E_tot"][0]))
    derive_N = np.max(np.abs(s["norme"] - s["norme"][0]))
    
    print(f"Dérive max de l'énergie totale : {derive_E:.2e}")
    print(f"Dérive max de la norme         : {derive_N:.2e}")
    
    # SEUILS DYNAMIQUES
    seuil_E = 1e-6
    seuil_N = 1e-6
    
    # ASSERTIONS
    assert derive_E < seuil_E, f"ÉCHEC : Dérive d'énergie trop grande ({derive_E:.2e} > {seuil_E})"
    assert derive_N < seuil_N, f"ÉCHEC : Dérive de norme trop grande ({derive_N:.2e} > {seuil_N})"
    
    print("-> SUCCÈS : Conservation de l'énergie et de la norme validée.")
