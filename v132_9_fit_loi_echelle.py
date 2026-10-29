import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N = 50
t_hop = 1.0
U = 1.0
WX, WZ = 0.5, 1.0
j0 = N // 2
NPART = 10.0
phi = 0.5

g_data = np.array([0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0])
activite_data = np.array([1.6386, 3.3309, 4.9941, 8.6402, 15.1753, 46.1321, 125.8555])

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
    Wc_plus = np.trapezoid(np.maximum(P_champ, 0), te)
    Wc_minus = np.trapezoid(np.maximum(-P_champ, 0), te)
    activite = Wc_plus + Wc_minus
    
    E_tot = E_kin + E_pot + E_q + E_int
    derive = np.max(np.abs(E_tot - E_tot[0]))
    
    return activite, derive

def model_power(g, alpha, C):
    return C * g**alpha

def model_exp(g, beta, C):
    return C * np.exp(beta * g)
    
def model_quad(g, C):
    return C * g**2

if __name__ == "__main__":
    print("=== V132.9 : Loi d'échelle et convergence ===\n")
    
    popt_power, _ = curve_fit(model_power, g_data, activite_data, p0=[2.0, 1.0], maxfev=10000)
    popt_exp, _ = curve_fit(model_exp, g_data, activite_data, p0=[1.0, 1.0], maxfev=10000)
    popt_quad, _ = curve_fit(model_quad, g_data, activite_data, p0=[1.0])
    
    print("--- Ajustement de l'activité A(g) ---")
    print(f"Puissance   : A = {popt_power[1]:.3f} * g^{popt_power[0]:.3f}")
    print(f"Exponentiel : A = {popt_exp[1]:.3f} * exp({popt_exp[0]:.3f} * g)")
    print(f"Quadratique : A = {popt_quad[0]:.3f} * g^2")
    
    res_power = np.sum((model_power(g_data, *popt_power) - activite_data)**2)
    res_exp = np.sum((model_exp(g_data, *popt_exp) - activite_data)**2)
    res_quad = np.sum((model_quad(g_data, *popt_quad) - activite_data)**2)
    
    print(f"\nRésidus (SSE) : Puissance={res_power:.1f} | Exponentiel={res_exp:.1f} | Quadratique={res_quad:.1f}")
    if res_power < res_exp and res_power < res_quad:
        print("-> Le modèle en puissance domine.")
    elif res_exp < res_power:
        print("-> Le modèle exponentiel domine.")
    else:
        print("-> Le modèle quadratique domine.")

    print("\n--- Test de convergence à g=5.0 ---")
    act_strict, err_strict = simulate(g_coupl=5.0, rtol=1e-11, atol=1e-12)
    act_loose, err_loose = simulate(g_coupl=5.0, rtol=1e-9, atol=1e-10)
    
    print(f"Activité (rtol=1e-11) : {act_strict:.4f}")
    print(f"Activité (rtol=1e-9)  : {act_loose:.4f}")
    print(f"Écart relatif : {abs(act_strict - act_loose)/act_strict * 100:.4f} %")
    print(f"Dérive Etot (strict)  : {err_strict:.2e}")
    
    g_plot = np.linspace(0.2, 5.2, 100)
    plt.figure(figsize=(10, 6))
    plt.plot(g_data, activite_data, 'ko', label="Données V132.8")
    plt.plot(g_plot, model_power(g_plot, *popt_power), 'b-', label=f"Puissance (alpha={popt_power[0]:.2f})")
    plt.plot(g_plot, model_exp(g_plot, *popt_exp), 'r--', label=f"Exponentiel (beta={popt_exp[0]:.2f})")
    plt.plot(g_plot, model_quad(g_plot, *popt_quad), 'g:', label="Quadratique")
    plt.title("Ajustement de l'activité du champ")
    plt.xlabel("Couplage g")
    plt.ylabel("Activité totale")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("v132_9_fits.png", dpi=150)
    print("\nFigure sauvegardée : v132_9_fits.png")
