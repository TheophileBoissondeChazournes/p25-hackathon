import numpy as np
import matplotlib.pyplot as plt

Nx = 50
Ny = 50
dx = 1.0 / (Nx - 1)
dy = 1.0 / (Ny - 1)

x = np.linspace(0, 1, Nx)
y = np.linspace(0, 1, Ny)
X, Y = np.meshgrid(x, y)

T = (
    12
    + np.sin(2 * np.pi * X) * np.sin(2 * np.pi * Y)
    - 21 * np.cos(2 * np.pi * X) * np.cos(2 * np.pi * Y)
)

dt = 0.2 * dx**2
alpha = dt / dx**2
Nt = 500


plt.ion()  # mode interactif
fig, ax = plt.subplots()

im = ax.imshow(
    T,
    extent=[0, 1, 0, 1],
    origin='lower',
    cmap='inferno',
    vmin=T.min(),
    vmax=T.max()
)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Température")

ax.set_xlabel("x")
ax.set_ylabel("y")

for n in range(Nt):

    Tn = T.copy()

    # Schéma explicite 2D (Laplacien)
    T[1:-1, 1:-1] = (Tn[1:-1, 1:-1]
        + alpha *  
        (Tn[2:, 1:-1] + Tn[:-2, 1:-1]
            + Tn[1:-1, 2:] + Tn[1:-1, :-2]
            - 4 * Tn[1:-1, 1:-1]))

    # Conditions de Dirichlet
    T[0, :] = 0
    T[-1, :] = 0
    T[:, 0] = 0
    T[:, -1] = 0

    # Mise à jour de l'affichage
    im.set_data(T)
    ax.set_title(f"Temps t = {n * dt:.4f}")

    plt.pause(0.01)

plt.ioff()
plt.show()
