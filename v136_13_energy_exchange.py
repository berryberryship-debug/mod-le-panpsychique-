"""
V136.13 — Bilan différentiel et échange d'énergie.
Vérifie que dE/dt ~ 0, que l'énergie circule (comparaison g=0), et teste la convergence.
"""
import numpy as np
from scipy.integrate import solve_ivp

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

def simulate(g_coupl, T=50.0, dt=0.05, rtol=1e-10, atol=1e-12):
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
        H_psi = H @ psi + U * np.abs(psi)**2 * psi
        if g_coupl > 0:
            H_psi[j0] += g_coupl * r[2] * psi[j0]
        dpsi = -1j * H_psi
        Omega = np.array([WX, 0.0, WZ + 2 * g_coupl * rho_j0])
        dr = np.cross(Omega, r)
        return np.concatenate([dpsi.real, dpsi.imag, dr])

    sol = solve_ivp(rhs, (0, T), y0, t_eval=te, method="DOP853", rtol=rtol, atol=atol)
    if not sol.success: 
        raise RuntimeError(f"Échec : {sol.message}")
        
    psi = sol.y[:N] + 1j * sol.y[N:2*N]
    r = sol.y[2*N:]
    
    phase = 2 * np.pi * phi / N
    E_kin = np.zeros_like(te)
    for j in range(N):
        j_next = (j + 1) % N
        E_kin += -2.0 * t_hop * np.real(np.conj(psi[j]) * np.exp(1j*phase) * psi[j_next])
        
    E_pot = 0.5 * U * np.sum(np.abs(psi)**4, axis=0)
    E_champ = E_kin + E_pot
    E_q = 0.5 * (WX * r[0] + WZ * r[2])
    E_int = g_coupl * np.abs(psi[j0])**2 * r[2] if g_coupl > 0 else np.zeros_like(te)
    E_tot = E_champ + E_q + E_int
    
    norme = np.sum(np.abs(psi)**2, axis=0)
    
    return dict(t=te, E_tot=E_tot, E_champ=E_champ, E_q=E_q, E_int=E_int, norme=norme)

if __name__ == "__main__":
    print("=== V136.13 : Bilan différentiel et échange ===")

    # 1. Test de convergence
    print("\n--- Test de convergence ---")
    s_ref = simulate(g_coupl=1.0, rtol=1e-10, atol=1e-12)
    s_loose = simulate(g_coupl=1.0, rtol=1e-8, atol=1e-10)
    
    diff_E_tot = np.max(np.abs(s_ref["E_tot"] - s_loose["E_tot"]))
    print(f"Écart max E_tot (rtol 1e-8 vs 1e-10) : {diff_E_tot:.2e}")
    assert diff_E_tot < 1e-4, "ÉCHEC : La solution dépend trop de la tolérance."
    print("-> SUCCÈS : Convergence validée.")

    # 2. Test du bilan différentiel (dE/dt = 0)
    print("\n--- Test du bilan différentiel ---")
    # On calcule la dérivée de E_tot par rapport au temps
    dE_dt = np.gradient(s_ref["E_tot"], s_ref["t"])
    max_dE_dt = np.max(np.abs(dE_dt))
    
    # La dérivée numérique introduit du bruit, on compare à l'échelle de E_tot
    print(f"Max |dE_tot/dt| : {max_dE_dt:.2e}")
    assert max_dE_dt < 1e-4, "ÉCHEC : L'énergie totale n'est pas constante (dE/dt trop grand)."
    print("-> SUCCÈS : Bilan différentiel validé.")

    # 3. Test de l'échange réel d'énergie
    print("\n--- Test de l'échange d'énergie (g=0 vs g=1) ---")
    s_0 = simulate(g_coupl=0.0)
    
    # Variations nettes sur toute la trajectoire
    delta_E_champ_0 = s_0["E_champ"][-1] - s_0["E_champ"][0]
    delta_E_champ_1 = s_ref["E_champ"][-1] - s_ref["E_champ"][0]
    
    # Si le couplage est actif, l'énergie du champ doit changer différemment
    diff_echange = abs(delta_E_champ_1 - delta_E_champ_0)
    
    print(f"Variation E_champ (g=0) : {delta_E_champ_0:.4f}")
    print(f"Variation E_champ (g=1) : {delta_E_champ_1:.4f}")
    print(f"Différence d'échange    : {diff_echange:.4f}")
    
    assert diff_echange > 0.01, "ÉCHEC : Le couplage ne modifie pas l'échange d'énergie."
    print("-> SUCCÈS : Le couplage induit un échange d'énergie réel.")

    print("\n--- TOUS LES TESTS SONT PASSÉS ---")
