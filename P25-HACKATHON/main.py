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
dt = 0.25 * min(dx*dx, dy*dy)
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
