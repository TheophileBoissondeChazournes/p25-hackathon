import time
import question_5
import question_5_explicite



print("Début du test explicite")


#On déclenche le chrono
debut = time.time()


question_5_explicite.explicite()

fin = time.time() 
    
temps_total = fin - debut
print(f"Pour explicite : {temps_total:.5f} sec")

print("Début du test implicite")


#On déclenche le chrono
debut = time.time()


question_5.implicite()

fin = time.time() 
    
temps_total = fin - debut
print(f"Pour implicite : {temps_total:.5f} sec")

