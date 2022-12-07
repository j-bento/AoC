nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    d={}
    d["A"]=1; d["X"]=1
    d["B"]=2; d["Y"]=2
    d["C"]=3; d["Z"]=3
    score = 0
    for line in f:
        adv, moi = line.split()
        if choix == 1:
            score+= d[moi]
            if (d[adv]%3)+1 == d[moi]:
                score+=6
            elif d[moi] == d[adv]:
                score+=3
        else:
            if moi == "Z":
                score+=(d[adv]%3)+7
            elif moi == "Y":
                score+=3+d[adv]
            else:
                if d[adv] == 1:
                    score+=3
                else:
                    score+=d[adv]-1
    print(score)
except FileNotFoundError:
    print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")