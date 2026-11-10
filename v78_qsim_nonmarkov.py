import numpy as np
import matplotlib.pyplot as plt


def run_v78_nonmarkov_physical():
    T = 20.0
    N = 1000
    time = np.linspace(0.0, T, N + 1)

    a = 0.75
    omega = 5.0

    # Taux instantané et taux intégré
    gamma = a * omega * np.sin(omega * time)
    Gamma = a * (1.0 - np.cos(omega * time))

    # Solution exacte pour rho(0) = |+><+|
    coherence = 0.5 * np.exp(-Gamma)

    rho = np.zeros((N + 1, 2, 2), dtype=complex)
    rho[:, 0, 0] = 0.5
    rho[:, 1, 1] = 0.5
    rho[:, 0, 1] = coherence
    rho[:, 1, 0] = coherence

    purities = np.real(
        np.einsum("tij,tji->t", rho, rho)
    )
    eigenvalues = np.linalg.eigvalsh(rho)
    traces = np.trace(rho, axis1=1, axis2=2)

    # Contrôles de validité physique
    assert np.min(Gamma) >= -1e-12
    assert np.min(eigenvalues) >= -1e-12
    assert np.allclose(traces, 1.0)
    assert np.allclose(rho, rho.conj().transpose(0, 2, 1))
    assert np.all(purities >= 0.5 - 1e-12)
    assert np.all(purities <= 1.0 + 1e-12)

    return time, gamma, Gamma, purities, eigenvalues


if __name__ == "__main__":
    time, gamma, Gamma, purities, eigenvalues = (
        run_v78_nonmarkov_physical()
    )

    print("V78 : déphasage à reprises périodiques de cohérence")
    print(f"Pureté minimale échantillonnée : {purities.min():.6f}")
    print(f"Pureté maximale échantillonnée : {purities.max():.6f}")
    print(f"Valeur propre minimale : {eigenvalues.min():.6e}")
    print(f"Taux intégré minimal : {Gamma.min():.6e}")

    fig, axes = plt.subplots(
        3, 1, figsize=(9, 9), sharex=True
    )

    axes[0].plot(time, gamma, color="darkorange")
    axes[0].axhline(0.0, color="black", linewidth=0.8)
    axes[0].set_ylabel("Taux gamma(t)")

    axes[1].plot(time, Gamma, color="teal")
    axes[1].set_ylabel("Taux intégré")

    axes[2].plot(time, purities, color="purple")
    axes[2].axhline(
        0.5, color="gray", linestyle="--",
        label="Pureté minimale d'un qubit"
    )
    axes[2].set_ylabel("Pureté")
    axes[2].set_xlabel("Temps — unités arbitraires")
    axes[2].legend()

    for ax in axes:
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        "V78 : canal de déphasage physique avec reprises de cohérence"
    )
    fig.tight_layout()
    fig.savefig("v78_nonmarkov_physical.png", dpi=180)
    plt.show()
