import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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

def simulate(g_coupl, unidirectional=False, T=50.0, dt=0.05, rtol=1e-9, atol=1e-10):
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
        
        if unidirectional:
            Omega = np.array([WX, 0.0, WZ]) 
        else:
            Omega = np.array([WX, 0.0, WZ + 2 * g_coupl * rho_j0])
            
        dr = np.cross(Omega, r)
            
        return np.concatenate([dpsi.real, dpsi.imag, dr])

    sol = solve_ivp(rhs, (0, T), y0, t_eval=te, method="DOP853", rtol=rtol, atol=atol)
    if not sol.success:
        raise RuntimeError(f"Échec solve_ivp : {sol.message}")
        
    psi = sol.y[:N] + 1j * sol.y[N:2*N]
    r = sol.y[2*N:]
    return dict(t=sol.t, psi=psi, r=r)

if __name__ == "__main__":
    print("=== V136.11 : Audit ciblé ===\n")
    
    print("--- Test de convergence (A vs D) ---")
    tolerances = [(1e-7, 1e-8), (1e-9, 1e-10), (1e-11, 1e-12)]
    
    resultats = []
    for rtol, atol in tolerances:
        s_A = simulate(g_coupl=1.0, unidirectional=False, rtol=rtol, atol=atol)
        s_D = simulate(g_coupl=1.0, unidirectional=True, rtol=rtol, atol=atol)
        
        D_psi = np.sqrt(np.sum(np.abs(s_A["psi"] - s_D["psi"])**2, axis=0))
        D_rho = np.sum(np.abs(np.abs(s_A["psi"])**2 - np.abs(s_D["psi"])**2), axis=0)
        D_r = np.sqrt(np.sum((s_A["r"] - s_D["r"])**2, axis=0))
        
        resultats.append({
            "rtol": rtol, "atol": atol,
            "max_D_psi": np.max(D_psi),
            "max_D_rho": np.max(D_rho),
            "max_D_r": np.max(D_r),
            "t": s_A["t"], "D_psi": D_psi, "D_rho": D_rho, "D_r": D_r
        })
        
        print(f"Tol {rtol:.0e} : max D_psi = {np.max(D_psi):.4f} | max D_rho = {np.max(D_rho):.4f} | max D_r = {np.max(D_r):.4f}")

    ref = resultats[1] 
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    
    axs[0].plot(ref["t"], ref["D_psi"], color='blue')
    axs[0].set_title("Distance des amplitudes (D_psi)")
    axs[0].set_xlabel("t")
    axs[0].grid(True, alpha=0.3)
    
    axs[1].plot(ref["t"], ref["D_rho"], color='orange')
    axs[1].set_title("Redistribution de densité (D_rho)")
    axs[1].set_xlabel("t")
    axs[1].grid(True, alpha=0.3)
    
    axs[2].plot(ref["t"], ref["D_r"], color='purple')
    axs[2].set_title("Distance des états de Bloch (D_r)")
    axs[2].set_xlabel("t")
    axs[2].grid(True, alpha=0.3)
    
    plt.suptitle("V136.11 : Effet de la rétroaction (A vs D)")
    plt.tight_layout()
    plt.savefig("v136_11_audit.png", dpi=150)
    print("\nFigure sauvegardée : v136_11_audit.png")
