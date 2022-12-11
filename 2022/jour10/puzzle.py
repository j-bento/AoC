from pathlib import Path

nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(str(Path(__file__).resolve().parent)+"/"+nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    cycles = 1 ; X = 1
    if choix == 1:
        cyclesResultats = []
        for line in f :
            spl = line.split()
            if spl[0] == "noop":
                cycles+=1
            else:
                cycles+=1
                if cycles in (20,60,100,140,180,220):
                    cyclesResultats.append(X*cycles)
                X+=int(spl[1])
                cycles+=1
            if cycles in (20,60,100,140,180,220):
                cyclesResultats.append(X*cycles)
        print(sum(cyclesResultats))
    else:
        CRT=""
        for line in f :
            spl = line.split()
            if spl[0] == "noop":
                cycles+=1
                lgCRT=len(CRT)%40
                if X in (lgCRT-1, lgCRT, lgCRT+1):
                    CRT+="#"
                else:
                    CRT+="."
            else:
                cycles+=1
                lgCRT=len(CRT)%40
                if X in (lgCRT-1, lgCRT, lgCRT+1):
                    CRT+="#"
                else:
                    CRT+="."

                cycles+=1
                lgCRT=len(CRT)%40
                if X in (lgCRT-1, lgCRT, lgCRT+1):
                    CRT+="#"
                else:
                    CRT+="."
                X+=int(spl[1])
        print(CRT[:40])
        print(CRT[40:80])
        print(CRT[80:120])
        print(CRT[120:160])
        print(CRT[160:200])
        print(CRT[200:240])
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")