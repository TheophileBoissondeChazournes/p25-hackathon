import time


pts = [100, 10000, 1000000]

print("Début du test de performance...")
print("-" * 40)

for N in pts:
    # On déclenche le chronomètre
    debut = time.time()

    # On simule le calcul sur N points
    for i in range(N):
        resultat = D(i)

    fin = time.time() 
    
    temps_total = fin - debut
    print(f"Pour {N:9} points : {temps_total:.5f} sec")

print("-" * 40)