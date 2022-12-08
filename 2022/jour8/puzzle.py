nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    if choix == 1:
        visibles= (len(lines)+len(lines[0])-2)*2
        for i in range(1,len(lines)-1):
            for j in range(1,len(lines[i])-1):
                gauche=any(int(lines[i][j]) <= int(lines[i][k]) for k in range(j))
                droite=any(int(lines[i][j]) <= int(lines[i][k]) for k in range(j+1,len(lines[i])))
                haut=any(int(lines[i][j]) <= int(lines[k][j]) for k in range(i))
                bas=any(int(lines[i][j]) <= int(lines[k][j]) for k in range(i+1,len(lines)))
                pasVisible = gauche and droite and haut and bas
                if not pasVisible:
                    visibles+=1
        print(visibles)
    else:
        maxi=0
        for i in range(1,len(lines)-1):
            for j in range(1,len(lines[i])-1):
                gauche, droite, haut, bas = 0, 0, 0, 0
                for k in range(j-1,-1,-1):
                    gauche+=1
                    if int(lines[i][j]) <= int(lines[i][k]):
                        break
                for k in range(j+1,len(lines[i])):
                    droite+=1
                    if int(lines[i][j]) <= int(lines[i][k]):
                        break
                for k in range(i-1,-1,-1):
                    haut+=1
                    if int(lines[i][j]) <= int(lines[k][j]):
                        break
                for k in range(i+1,len(lines)):
                    bas+=1
                    if int(lines[i][j]) <= int(lines[k][j]):
                        break
                scenicScore=gauche*droite*haut*bas
                if scenicScore > maxi:
                    maxi=scenicScore
        print(maxi)
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")