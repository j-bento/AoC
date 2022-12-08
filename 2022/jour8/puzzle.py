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
    visibles= (len(lines)+len(lines[0])-2)*2
    print(lines, visibles)
    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[i])-1):
            # pasVisible=True
            
            visible=all(int(lines[i][j]) <= int(k) for k in lines[i][:j]) and all( int(lines[i][j]) <= int(k[:j]) for k in lines) and all(int(lines[i][j]) <= int(k) for k in lines[i][j:]) and all( int(lines[i][j]) <= int(k[j:]) for k in lines)
            # for k in range(len(lines[i])):
            #     if lines[i][k] < lines[i][j] and k!=j:
            #         pasVisible=False
            #         print("ici",lines[i][k], lines[i][j])
            #         break
            # if pasVisible:
            #     for k in range(len(lines)):
            #         if lines[k][j] < lines[i][j] and k!=i:
            #             pasVisible=False
            #             print("ici2",lines[i][k], lines[i][j])
            #             break
            if visible:
                print("lines[",i,"][",j,"] :",lines[i][j])
                visibles+=1
    print(visibles)
            
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
# except ValueError:
#     print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")