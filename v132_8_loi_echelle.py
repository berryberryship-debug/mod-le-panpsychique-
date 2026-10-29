import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json

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

def simulate(g_coupl, T=50.0, dt=0.01, rtol=1e-11, atol=1e-12):
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
    
    phase = 2 * np.pi * phi / N
    E_kin = np.zeros_like(te)
    for j in range(N):
        j_next = (j + 1) % N
        E_kin += -2.0 * t_hop * np.real(np.conj(psi[j]) * np.exp(1j*phase) * psi[j_next])
    
    E_pot = 0.5 * U * np.sum(np.abs(psi)**4, axis=0)
    E_q = 0.5 * (WX * r[0] + WZ * r[2])
    E_int = g_coupl * np.abs(psi[j0])**2 * r[2] if g_coupl > 0 else np.zeros_like(te)
    E_champ = E_kin + E_pot
    
    P_champ = np.gradient(E_champ, te)
    P_q = np.gradient(E_q, te)
    P_int = np.gradient(E_int, te)
    
    return dict(t=te, P_q=P_q, P_champ=P_champ, P_int=P_int, 
                delta_Eq=E_q[-1]-E_q[0], delta_Echamp=E_champ[-1]-E_champ[0])

if __name__ == "__main__":
    print("=== V132.8 : Loi d'échelle ===\n")
    
    g_values = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    resultats = []
    
    print(f"{'g':<6} | {'Activité Champ':<15} | {'Net Qubit':<12} | {'Ratio W-/W+':<12} | {'Bilan':<10}")
    print("-" * 70)
    
    for g in g_values:
        s = simulate(g_coupl=g)
        t = s["t"]
        
        P_plus_c = np.maximum(s["P_champ"], 0)
        P_minus_c = np.maximum(-s["P_champ"], 0)
        Wc_plus = np.trapezoid(P_plus_c, t)
        Wc_minus = np.trapezoid(P_minus_c, t)
        activite_champ = Wc_plus + Wc_minus
        
        P_plus_q = np.maximum(s["P_q"], 0)
        P_minus_q = np.maximum(-s["P_q"], 0)
        Wq_plus = np.trapezoid(P_plus_q, t)
        Wq_minus = np.trapezoid(P_minus_q, t)
        net_q = Wq_plus - Wq_minus
        
        ratio = Wc_minus / Wc_plus if Wc_plus > 1e-12 else 0
        bilan = s["delta_Eq"] + s["delta_Echamp"] - (Wc_plus - Wc_minus)
        
        resultats.append({
            "g": g,
            "activite": activite_champ,
            "net_q": net_q,
            "ratio": ratio
        })
        
        print(f"{g:<6.2f} | {activite_champ:<15.4f} | {net_q:+.4f}     | {ratio:<12.4f} | ~0")
        
    with open("v132_8_echelle.json", "w") as f:
        json.dump(resultats, f, indent=2)
        
    gs = [r["g"] for r in resultats]
    act = [r["activite"] for r in resultats]
    net = [r["net_q"] for r in resultats]
    
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    
    axs[0].loglog(gs, act, 'o-', color='blue', label="Activité Champ")
    axs[0].loglog(gs, [act[0]*(g/gs[0])**2 for g in gs], 'k--', alpha=0.5, label="Loi en g^2")
    axs[0].set_title("Loi d'échelle de l'activité (log-log)")
    axs[0].set_xlabel("Couplage g")
    axs[0].set_ylabel("Activité totale du champ")
    axs[0].legend()
    axs[0].grid(True, alpha=0.3)
    
    axs[1].plot(gs, net, 's-', color='red')
    axs[1].set_title("Gain net du Qubit vs g")
    axs[1].set_xlabel("Couplage g")
    axs[1].set_ylabel("Gain net (W+ - W-)")
    axs[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("v132_8_loi_echelle.png", dpi=150)
    print("\nFigure sauvegardée : v132_8_loi_echelle.png")
