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
        x1=l[0];x2=l[2]
        y1=l[1];y2=l[3]
        #verif x1=x2 ou y1=y2
        if x1==x2 or y1==y2:#horizontal ou vertical
            if y1==y2:#pour les x
                while x1!=x2:
                    grid[y1][x1]+=1
                    if x1<x2:
                        x1+=1
                    else:
                        x1-=1 
                grid[y1][x1]+=1 
            
            elif x1==x2:#pour les y
                while y1!=y2:
                    grid[y1][x1]+=1
                    if y1<y2:
                        y1+=1
                    else:
                        y1-=1 
                grid[y1][x1]+=1   
        elif x1<x2 and y1<y2: #diagonales #(1,1 -> 3,3)
            while x1<=x2:
                grid[y1][x1]+=1
                x1+=1
                y1+=1
        elif x1>x2 and y1>y2: #(3,3 -> 1,1)
            while x1>=x2:
                grid[y1][x1]+=1
                x1-=1
                y1-=1
        elif x1<x2 and y1>y2: #(7,9 -> 9,7)
            while x1<=x2:
                grid[y1][x1]+=1
                x1+=1
                y1-=1
        elif x1>x2 and y1<y2: #(9,7 -> 7,9)
            while x1>=x2:
                grid[y1][x1]+=1
                x1-=1
                y1+=1
    return grid

def compte(grid): # compte le nombre de cases supérieures à 2    
    cpt=0
    for i in grid:
        for elt in i:
            if elt>1:
                cpt+=1
    return cpt

ok=calc_diag(T)
# affiche(ok)
print(compte(ok))