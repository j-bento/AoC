cptI=0;cptD=0#compteur Increase/Decrease
with open('input') as f:
    precedent=f.readline()
    for line in f:
        if int(precedent)<int(line):
            cptI+=1
        elif int(precedent)>int(line):
            cptD+=1
        precedent=line
print(cptI,cptD)
