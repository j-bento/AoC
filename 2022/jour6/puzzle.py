nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich)
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    line = f.readline()
    if choix == 1:
        for i in range(len(line)-3):
            tmpLine=line[i:i+4]
            noDuplicates=True
            for car in tmpLine:
                if tmpLine.count(car) > 1:
                    noDuplicates=False
            if noDuplicates :
                break
        print(line[i:i+4],i+4)
    else:
        for i in range(len(line)-13):
            tmpLine=line[i:i+14]
            noDuplicates=True
            for car in tmpLine:
                if tmpLine.count(car) > 1:
                    noDuplicates=False
            if noDuplicates :
                break
        print(line[i:i+14],i+14)
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")