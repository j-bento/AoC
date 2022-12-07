from treelib import Node, Tree
nom_fich = input("Choisissez sur quel input tester la solution (i ou it): ")
try:
    f=open(nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    f.readline() # première ligne '$ cd /' inutile
    systemeFichiers = Tree()

    def poidsDossier(sf:Tree,noeudCourant:Node):
        newsf=sf.subtree(noeudCourant._identifier)
        feuilles = newsf.leaves()
        somme=0
        for feuille in feuilles:
            somme+=feuille.data
        return somme
        
    noeudCourant=Node("/")
    systemeFichiers.add_node(noeudCourant)
    # construction de l'arbre
    for line in f:
        spl = line.split()
        if spl[0] == "$": # commande
            if spl[1] == "cd": # cd
                if spl[2] == "..":
                    noeudCourant=systemeFichiers.parent(noeudCourant._identifier)
                else: # $ cd <dossier>
                    noeudsEnfants=systemeFichiers.children(noeudCourant._identifier)
                    for noeud in noeudsEnfants:
                        if noeud.tag == spl[2]:
                            noeudCourant = noeud
                            break
        else:
            if spl[0] == "dir":
                systemeFichiers.create_node(spl[1], parent=noeudCourant.identifier)
            else: # un fichier sinon
                systemeFichiers.create_node(spl[1]+" (file, size="+spl[0]+")", parent=noeudCourant.identifier, data=int(spl[0]))    
    systemeFichiers.show()
    if choix == 1:
        somme=0
        for noeud in systemeFichiers.all_nodes():
            if not noeud.is_leaf():
                pds = poidsDossier(systemeFichiers,noeud)
                if pds < 100000:
                    somme+=pds
        print("Somme des fichiers de taille < 100 000 :",somme)
    else:
        n = systemeFichiers.get_node(systemeFichiers.root)
        mini = poidsDossier(systemeFichiers,n)
        aSupprimer = mini-40000000
        print("total occupé :",mini,", quantité à supprimer :",aSupprimer)
        for noeud in systemeFichiers.all_nodes():
            if not noeud.is_leaf():
                pds = poidsDossier(systemeFichiers,noeud)
                if pds > aSupprimer and pds < mini :
                    mini = pds
                    n = noeud
        print("dossier sélectionné :",n.tag, mini)
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")