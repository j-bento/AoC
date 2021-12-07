with open('i') as f:
    crabs=[int(i) for i in f.readline().split(',')]
f.close()

#calcul le fuel dépensé pour atteindre une position pour tous les crabes
def calculFuel(crabs,position):
    fuel=0
    for i in crabs:
        fuel+= abs(i-position)
    return fuel

#solution légèrement brute force
maxi=max(crabs)
res=min([calculFuel(crabs,i) for i in range(maxi+1)])
print("résultat:",res)