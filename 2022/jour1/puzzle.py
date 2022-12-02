nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich)
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    lines = [i.split("\n")[0] for i in (f.readlines())]
    calories=[0]
    for line in lines:
        if line != "":
            calories[len(calories)-1] += (int(line))
        else:
            calories.append(0)
    if choix == 1:
        print(max(calories))
    else:
        elf1 = calories.pop(calories.index(max(calories)))
        elf2 = calories.pop(calories.index(max(calories)))
        elf3 = calories.pop(calories.index(max(calories)))
        print(elf1+elf2+elf3)
except FileNotFoundError:
    print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")