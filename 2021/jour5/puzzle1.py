T=[]
with open('i') as f:
    for line in f:
        Ti=[]
        Ti+=[int(i) for i in line.split(" -> ")[0].split(',')]
        Ti+=[int(i) for i in line.split(" -> ")[1].split(',')]
        T.append(Ti)
# print(T)
#affiche la grille des vents
def affiche(grid):
    for ligne in grid:
        for elt in ligne:
            if elt==0:
                print(".",end="")
            else:
                print(elt,end="")
        print()

#calcule la grille des vents
def calc_diag(tuples):
    grid=[[0]*1000 for i in range(1000)]
    for l in tuples: #l: ligne
        #verif x1=x2 ou y1=y2
        if l[0]==l[2] or l[1]==l[3]:
            if l[1]==l[3]:#pour les x
                while l[0]!=l[2]:
                    grid[l[1]][l[0]]+=1
                    if l[0]<l[2]:
                        l[0]+=1
                    else:
                        l[0]-=1 
                grid[l[1]][l[0]]+=1 
            
            elif l[0]==l[2]:#pour les y
                while l[1]!=l[3]:
                    grid[l[1]][l[0]]+=1
                    if l[1]<l[3]:
                        l[1]+=1
                    else:
                        l[1]-=1 
                grid[l[1]][l[0]]+=1   
    return grid
# grid=[[0]*10 for i in range(10)]
# affiche(grid)
ok=calc_diag(T)
cpt=0
for i in ok:
    for elt in i:
        if elt>1:
            cpt+=1
# affiche(ok)
print(cpt)