nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    res=0
    if choix == 1:
        for line in f:
            range1, range2 = line.split(',')
            s = range1.split('-')
            sl1= int(s[0])
            sl2= int(s[1])
            s = range2.split('-')
            sr1= int(s[0])
            sr2= int(s[1])
            if (sl1 >= sr1 and sl2 <= sr2) or (sr1 >= sl1 and sr2 <= sl2):
                res+=1
        print(res)
    else:
        for line in f:
            range1, range2 = line.split(',')
            s = range1.split('-')
            sl1= int(s[0])
            sl2= int(s[1])
            s = range2.split('-')
            sr1= int(s[0])
            sr2= int(s[1])
            if ((sl1 >= sr1 and sl1 <= sr2) or (sl2 >= sr1 and sl2 <= sr2)) or ((sr1 >= sl1 and sr1 <= sl2) or (sr2 >= sl1 and sr2 <= sl2)):
                res+=1
        print(res)
    ####################################################
except FileNotFoundError:
    print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")