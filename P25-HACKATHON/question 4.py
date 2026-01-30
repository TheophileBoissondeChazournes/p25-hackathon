import numpy as np
import matplotlib.pyplot as plt
import question3 



L = 1.0          
Nx = 20            # Nombre de x
Ny = 20            # Nombre de y
dx = L / (Nx - 1)  
dy = L / (Ny - 1)  
D = 1.0            #Coeff de diffusion  
dt = 0.01         
t_final = 0.1      #Temps total  
Nt = int(t_final / dt) #Nombre d'étapes


#initialisation de la température
T = np.zeros((Ny, Nx))

#remplissage point par point
for j in range(Ny):
    y = j * dy #Position y actuelle
    for i in range(Nx):
        x = i * dx #Position x actuelle
        #Formule : T = 1/2 + sin(2pi*x)*sin(2pi*y) - 1/2*cos(2pi*x)*cos(2pi*y)
        T[j, i] = 0.5 + np.sin(2*np.pi*x) * np.sin(2*np.pi*y) - 0.5 * np.cos(2*np.pi*x) * np.cos(2*np.pi*y)
        

#conditions limites 
for i in range(Nx):
    T[0, i] = 0      #Bord bas
    T[Ny-1, i] = 0   #Bord haut
for j in range(Ny):
    T[j, 0] = 0      #Bord gauche
    T[j, Nx-1] = 0   #Bord droit

#transformation de la grille en vecteur
T_vec = T.flatten()
N_tot = Nx * Ny


#Cette matrice représente les dérivées spatiales
K = np.zeros((N_tot, N_tot))

for j in range(1, Ny - 1):
    for i in range(1, Nx - 1):
        idx = i + j * Nx #Indice (i,j) dans le vecteur plat
        
        #Remplissage selon le schéma des différences finies 
        K[idx, idx] = 2*D/dx**2 + 2*D/dy**2     # Point central
        K[idx, idx-1] = -D/dx**2                # Voisin gauche
        K[idx, idx+1] = -D/dx**2                # Voisin droite
        K[idx, idx-Nx] = -D/dy**2               # Voisin bas
        K[idx, idx+Nx] = -D/dy**2               # Voisin haut

#Pour Euler Implicite, on doit résoudre (I + dt*K) * T_suivant = T_actuel 
A = np.eye(N_tot) + dt * K

historique_T = []

for k in range(Nt):
    #on réutilise la question 3
    T_vec = question3.grad_conj(A, T_vec)
    
    #Forcer les bords à 0 
    for i in range(N_tot):
        col, lig = i % Nx, i // Nx
        if col == 0 or col == Nx-1 or lig == 0 or lig == Ny-1:
            T_vec[i] = 0
            
   
    historique_T.append(T_vec.copy().reshape((Ny, Nx)))


indice_x = Nx // 2 #on peut changer le x qui nous intéresse, ici on prend au milieu

#On crée une matrice vide pour stocker T en fonction de (y, t)
Z = np.zeros((Nt, Ny))

for k in range(Nt):
    #Pour chaque instant k, on prend la colonne correspondant à notre x
    Z[k, :] = historique_T[k][:, indice_x]

#Affichage de l'évolution temporelle
plt.figure(figsize=(8, 6))
plt.imshow(Z, aspect='auto', extent=[0, L, t_final, 0], cmap='hot')
plt.colorbar(label="Température")
plt.xlabel("y")
plt.ylabel("t")
plt.title(f"température en fonction du temps (x={indice_x*dx:.2f})")
plt.show()