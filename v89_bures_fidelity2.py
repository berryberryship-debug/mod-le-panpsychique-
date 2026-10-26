```python
import numpy as np
import qutip as qt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("=== V89 : BALAYAGE DE GAMMA (Fidélité de Bures) ===", flush=True)

T_FINAL = 20.0
N_STEPS = 400
OMEGA = 1.0
THETA = np.pi / 3.0
GAMMA_SWEEP = np.linspace(0.0, 0.5, 51)

sx, sy, sz = qt.sigmax(), qt.sigmay(), qt.sigmaz()

def hamiltonian(phi):
    nx = np.sin(THETA) * np.cos(phi)
    ny = np.sin(THETA) * np.sin(phi)
    nz = np.cos(THETA)
    return 0.5 * OMEGA * (nx * sx + ny * sy + nz * sz)

def ground_state(phi):
    energies, states = hamiltonian(phi).eigenstates()
    return states[int(np.argmin(energies))]

def simulate(gamma):
    times = np.linspace(0.0, T_FINAL, N_STEPS + 1)
    def H_of_t(t, **kwargs):
        phi = 2.0 * np.pi * t / T_FINAL
        return hamiltonian(phi)
    psi0 = ground_state(0.0)
    rho0 = psi0.proj()
    c_ops = [np.sqrt(gamma / 2.0) * sz] if gamma > 0 else []
    result = qt.mesolve(H_of_t, rho0, times, c_ops=c_ops,
                        options={"store_states": True, "atol": 1e-10, "rtol": 1e-9})
    return result.states

rhos_ideal = simulate(0.0)
rho_ideal_final = rhos_ideal[-1]
rho_initial = rhos_ideal[0]

purities = []
bures_ideal = []
bures_initial = []
bures_angle = []

for gamma in GAMMA_SWEEP:
    rhos = simulate(gamma)
    rho_final = rhos[-1]
    purity = float(np.real((rho_final * rho_final).tr()))
    F_ideal = qt.fidelity(rho_final, rho_ideal_final)
    F_init = qt.fidelity(rho_final, rho_initial)
    theta = np.arccos(np.clip(F_ideal, 0.0, 1.0))
    
    purities.append(purity)
    bures_ideal.append(F_ideal)
    bures_initial.append(F_init)
    bures_angle.append(theta)

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

axes[0].plot(GAMMA_SWEEP, purities, 'o-', color='#2ca02c', markersize=4)
axes[0].axhline(0.5, color='gray', linestyle='--', alpha=0.5, label='I/2')
axes[0].set_xlabel(r"Taux de décohérence \(\gamma\)")
axes[0].set_ylabel(r"Pureté finale \(\mathrm{Tr}(\rho^2)\)")
axes[0].set_title("Plénitude (Pureté)")
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].plot(GAMMA_SWEEP, bures_ideal, 'o-', color='#d62728', markersize=4, label='vs Idéal')
axes[1].plot(GAMMA_SWEEP, bures_initial, 's--', color='#9467bd', markersize=4, alpha=0.6, label='vs Initial')
axes[1].set_xlabel(r"Taux de décohérence \(\gamma\)")
axes[1].set_ylabel(r"Fidélité de Bures \(F_B\)")
axes[1].set_title("Similarité Géométrique")
axes[1].legend()
axes[1].grid(alpha=0.3)

axes[2].plot(GAMMA_SWEEP, bures_angle, 'o-', color='#1f77b4', markersize=4)
axes[2].set_xlabel(r"Taux de décohérence \(\gamma\)")
axes[2].set_ylabel(r"Angle de Bures \(\theta = \arccos(F_B)\) (rad)")
axes[2].set_title("Distance Géodésique à l'Idéal")
axes[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig("v89_bures_fidelity.png", dpi=150)
np.savez("v89_bures_data.npz", gamma=GAMMA_SWEEP, purity=purities,
         bures_ideal=bures_ideal, bures_initial=bures_initial, bures_angle=bures_angle)
```
