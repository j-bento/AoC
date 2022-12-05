nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich)
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    stacks_nb = len(f.readline())//4
    f.seek(0)
    stacks=[[] for _ in range(stacks_nb) ]
    for line in f:
        if line.split()[0] in "123456789":
            break
        for i in range(0,len(line),4):
            if "[" in line[i:i+3]:
                stacks[i//4].append(line[i:i+3])
    for i in range(stacks_nb):
        stacks[i].reverse()
    f.readline()
    if choix == 1:
        for line in f:
            spl = line.split()
            nb , stackSrc, stackDest = int(spl[1]), int(spl[3])-1, int(spl[5])-1
            for i in range(nb):
                stacks[stackDest].append(stacks[stackSrc].pop())
    else:
        for line in f:
            spl = line.split()
            nb , stackSrc, stackDest = int(spl[1]), int(spl[3])-1, int(spl[5])-1
            stacks[stackDest]+=stacks[stackSrc][-nb:len(stacks[stackSrc])]
            del stacks[stackSrc][-nb:len(stacks[stackSrc])]
    for i in range(stacks_nb):
        if stacks[i]:
            print(stacks[i][-1],end=" ")
    print()
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")