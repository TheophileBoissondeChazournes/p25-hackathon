import numpy as np
import matplotlib.pyplot as plt

# Paramètres
Nx, Ny = 20, 20
L = 1.0
D = 0.5 + np.random.rand(Nx-2)
t_final = 0.5

dx = L/(Nx-1)
dy = L/(Ny-1)
dt = 0.25 * min(dx*dx, dy*dy)  # condition de stabilité
Nt = int(t_final/dt)

# Initialisation de la matrice T
x = np.linspace(0, L, Nx)
y = np.linspace(0, L, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')
T = 0.5 + np.sin(2*np.pi*X)*np.sin(2*np.pi*Y) - 0.5*np.cos(2*np.pi*X)*np.cos(2*np.pi*Y)

# Conditions aux limites
T[0,:] = T[-1,:] = T[:,0] = T[:,-1] = 0

# Ouverture fichier
f_all = open("results.txt", "w")

# Boucle temporelle
for n in range(Nt+1):
    t = n*dt

    # Sauvegarde 
    t_col = np.full_like(X, t)
    np.savetxt(f_all, np.column_stack((t_col.ravel(), 
                                       np.repeat(np.arange(Nx), Ny), 
                                       np.tile(np.arange(Ny), Nx), 
                                       X.ravel(), Y.ravel(), T.ravel())),
               fmt="%.6f %.0f %.0f %.6f %.6f %.6f")

    if n == Nt:
        break

    # Euler explicite
    Tnew = T.copy()
    Tnew[1:-1,1:-1] = T[1:-1,1:-1] + dt*D*(
        (T[2:,1:-1] - 2*T[1:-1,1:-1] + T[:-2,1:-1])/dx**2 +
        (T[1:-1,2:] - 2*T[1:-1,1:-1] + T[1:-1,:-2])/dy**2
    )

    # Conditions aux limites
    Tnew[0,:] = Tnew[-1,:] = Tnew[:,0] = Tnew[:,-1] = 0
    T = Tnew

f_all.close()
print("Fichier results.txt créé avec toute la grille.")

# Affichage
x_choice = 0.8
data = np.loadtxt("results.txt", comments="#")
t_vals = np.unique(data[:,0])
y_vals = np.unique(data[:,4])
x_vals = np.unique(data[:,3])
ix = np.argmin(np.abs(x_vals - x_choice))
x_nearest = x_vals[ix]
print(f"x choisi = {x_choice}, x utilisé = {x_nearest}")

# Construction matrice T(y,t) vectorisée
mask_x = data[:,3]==x_nearest
Tmat = data[mask_x,5].reshape(len(t_vals), len(y_vals))

# Affichage T(y,t)
plt.figure(figsize=(6,5))
plt.imshow(Tmat, aspect='auto', extent=[y_vals[0], y_vals[-1], t_vals[-1], t_vals[0]])
plt.colorbar(label="T")
plt.xlabel("y")
plt.ylabel("t")
plt.title(f"T(y,t) pour x = {x_nearest:.3f}")
plt.show()

# T(t) au milieu
y_mid_idx = len(y_vals)//2
plt.figure()
plt.plot(t_vals, Tmat[:, y_mid_idx], marker='o')
plt.xlabel("t")
plt.ylabel("T")
plt.title(f"T(t) en x={x_nearest:.3f}, y≈{y_vals[y_mid_idx]:.3f}")
plt.grid(True)
plt.show()