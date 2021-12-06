import time
# lFs: lantern fishs
with open('it') as f:
    lFs=[int(i) for i in f.readline().split(',')]
f.close()

#calcule la population du jour suivant
def nextDay(lFs):
    for lF in range(len(lFs)):
        lFs[lF]-=1
        if lFs[lF]<0:
            lFs[lF]=6
            lFs.append(8)
    return lFs

#pas plus opti...
def nextDayV2(lFs):
    nbr=lFs.count(0)
    lFs=[i-1 if (i-1)>=0 else 6 for i in lFs]
    lFs+=[8]*nbr
    return lFs

# donne la population de lanterns fishs étant donné une liste de lanterns fishs et un nombre de jours
# solution naïve
def simulation(lFs,days):
    for i in range(days):
        lFs=nextDay(lFs)
    return lFs

t1=time.time()
resultat=simulation(lFs,80)
t2=time.time()

print(len(resultat))
print(t2-t1,"seconde(s)")

#trop lent :/
# t1=time.time()
# resultat=simulation(lFs,85)
# t2=time.time()

# print(len(resultat))
# print(t2-t1,"seconde(s)")