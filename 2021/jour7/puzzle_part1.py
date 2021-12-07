from collections import Counter

with open('i') as f:
    crabs=[int(i) for i in f.readline().split(',')]
f.close()

count=Counter(crabs)
#position horizontale la plus commune pour tous les crabes
plus_commun=count.most_common(1)[0][0]
plus_commun2=count.most_common(2)[1][0]

#calcul le fuel dépensé pour atteindre une position pour tous les crabes
def calculFuel(crabs,position):
    fuel=0
    for i in crabs:
        fuel+= abs(i-position)
    return fuel

res=min()
for i in count:
    print(i)
fuel=calculFuel(crabs,plus_commun)
fuel2=calculFuel(crabs,plus_commun2)
print("indice le plus commun:",plus_commun)
print("carburant minimum:",fuel)

print("indice le plus commun 2:",plus_commun2)
print("carburant minimum 2:",fuel2)
