#recupération tirages et grilles
grilles=[]
with open('i') as f:
    tirages=[int(i) for i in f.readline().split(',')]
    f.readline()
    for line in f:
        grilles+=[int(i) for i in line.split()]

#mise des grilles au bon format
G=[]
for i in range(0,len(grilles),25):
    gr=[]
    for j in range(25):
        gr.append(grilles[i+j])
    G.append(gr)

#regarde si une grille a un bingo horizontal/vertical selon une liste d'elt tirés
def verif(grille,tires):
    # print()
    oui=0 #nbr de fois ou l'elt tiré est dans une ligne de la grille
    for i in range(0,len(grille),5):#verif horizontale
        oui=0
        for j in range(5):
            if grille[i+j] in tires:
                oui+=1
        # print(oui)
        if oui==5:
            return True
    # print()
    for i in range(5):
        oui=0 #nbr de fois ou l'elt tiré est dans une colonne de la grille
        for j in range(0,len(grille),5):
            if grille[i+j] in tires:
                oui+=1
        # print(oui)
        if oui==5:
            return True
    return False
    

#tirages:
tires=[] #les numéros tirés
i=0
while not verif(G[i],tires) and tirages:
    i+=1
    if i==len(G):#on a essayé pour toutes les grilles -> on passe au tirage suivant
        i=0 
        tires.append(tirages[0])
        tirages.remove(tirages[0])
    
nontires=sum([j for j in G[i] if j not in tires])
print(nontires,tires[len(tires)-1],nontires*tires[len(tires)-1])