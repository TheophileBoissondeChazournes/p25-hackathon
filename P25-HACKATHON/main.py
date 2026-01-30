import numpy as np
import matplotlib.pyplot as plt

#Paramètres
Nx = 20
Ny = 20
L = 1.0
D = 1.0
t_final = 0.1

dx = L/(Nx-1)
dy = L/(Ny-1)
dt = 0.25 * min(dx*dx, dy*dy) #vérifie la condition de stabilité
Nt = int(t_final/dt)

# On initialise
T = np.zeros((Nx, Ny))
for i in range(Nx):
    for j in range(Ny):
        x = i*dx
        y = j*dy
        T[i,j] = 0.5 + np.sin(2*3.14*x)*np.sin(2*3.14*y) - 0.5*np.cos(2*3.14*x)*np.cos(2*3.14*y)
T[0,:]=T[-1,:]=T[:,0]=T[:,-1]=0

# On ouvre le fichier pour écrire tous les résultats
f_all = open("results.txt","w")

# boucle temporelle
for n in range(Nt+1):
    t = n*dt

    # sauvegarde
    for i in range(Nx):
        for j in range(Ny):
            f_all.write(f"{t} {i} {j} {i*dx} {j*dy} {T[i,j]}\n")

    if n == Nt:
        break  # pour arreter après la dernière sauvegarde

    # Euler explicite
    Tnew = T.copy()
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            Tnew[i,j] = T[i,j] + dt*D*(
                (T[i+1,j]-2*T[i,j]+T[i-1,j])/dx**2 +
                (T[i,j+1]-2*T[i,j]+T[i,j-1])/dy**2
            )

    # On remet les conditions aux limites
    Tnew[0,:]=Tnew[-1,:]=Tnew[:,0]=Tnew[:,-1]=0

    T = Tnew

f_all.close()
print("Fichier results.txt créé avec toute la grille.")

#On fait l affichage 


# choix du x
x_choice = 0.8 


# On reprend notre fichier
data = np.loadtxt("results.txt", comments="#")

# On définit nos vecteurs
t_vals = np.unique(data[:,0])
y_vals = np.unique(data[:,4])

# On adapte x pour trouver le plus proche
x_vals = np.unique(data[:,3])
ix = np.argmin(np.abs(x_vals - x_choice))
x_nearest = x_vals[ix]
print(f"x choisi = {x_choice}, x utilisé = {x_nearest}")


#On construit notre matrice T(y,t)
Tmat = np.zeros((len(t_vals), len(y_vals)))

for n, t in enumerate(t_vals):
    for j, y in enumerate(y_vals):
        mask = (data[:,0]==t) & (data[:,3]==x_nearest) & (data[:,4]==y)
        Tmat[n,j] = data[mask,5][0]

#On affiche le résultat
plt.figure(figsize=(6,5))
plt.imshow(Tmat, aspect='auto', extent=[y_vals[0], y_vals[-1], t_vals[-1], t_vals[0]])
plt.colorbar(label="T")
plt.xlabel("y")
plt.ylabel("t")
plt.title(f"T(y,t) pour x = {x_nearest:.3f}")
plt.show()

#on affiche T en fonction de t pour y milieu de la ligne
y_mid_idx = len(y_vals)//2
plt.figure()
plt.plot(t_vals, Tmat[:, y_mid_idx], marker='o')
plt.xlabel("t")
plt.ylabel("T")
plt.title(f"T(t) en x={x_nearest:.3f}, y≈{y_vals[y_mid_idx]:.3f}")
plt.grid(True)
plt.show()
