nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich)
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    res=0
    if choix == 1:
        for line in f:
            comp1, comp2 = line[:int(len(line)/2)], line[int(len(line)/2):]
            for car in comp1:
                if car in comp2:
                    res+=ord(car)
                    if car.isupper():
                        res-=38
                    else:
                        res-=96
                    break
        print(res)
    else:
        lines = [i.replace('\n',"") for i in f.readlines()]
        for i in range(0, len(lines), 3):
            comp = lines[i:i+3]
            for car in comp[0]:
                if car in comp[1] and car in comp[2]:
                    res+=ord(car)
                    if car.isupper():
                        res-=38
                    else:
                        res-=96
                    break
        print(res)
    ####################################################
except FileNotFoundError:
    print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")