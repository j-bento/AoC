import time
from collections import Counter
# lFs: lantern fishs
with open('i') as f:
    lFs=[int(i) for i in f.readline().split(',')]
f.close()

# recomptage du nombre d'elts pour tous les niveaux de timers internes pour chaque nouveau jour
# timers internes allant de 0 à 8
def simulation(lFs,days):
    count = Counter(lFs)
    for _ in range(days):
        zeros = count[0]
        for i in range(7):
            count[i]=count[i+1]
        count[6] += zeros
        count[7] = count[8]
        count[8] = zeros
    return count

t1=time.time()
resultat=simulation(lFs,256)
t2=time.time()
print(sum(i for i in resultat.values()))
print(t2-t1,"seconde(s)")