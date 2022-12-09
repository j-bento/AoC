from pathlib import Path

nom_fich = input("Choisissez sur quel input tester la solution (i ou it ou it2 (input test partie 2)): ")

class Position:
    x=0
    y=0
    countVisits=False
    visited=["0 0"]
    def __repr__(self) -> str:
        return "Pos("+str(self.x)+ ", " + str(self.y)+")"

    def moveTo(self,pos2):
        while not self.nextTo(pos2):
            if self.x == pos2.x: # aligné verticalement
                if pos2.y > self.y: # self va à droite
                    self.y += 1
                else: # self va à gauche
                    self.y -= 1
            elif self.y == pos2.y: # aligné horizontalement
                if pos2.x > self.x: # self monte
                    self.x += 1
                else: # self descend
                    self.x -= 1
            else: # diagonal
                if pos2.x > self.x:
                    self.x+=1
                else:
                    self.x-=1
                if pos2.y > self.y:
                    self.y+=1
                else:
                    self.y-=1
            if self.countVisits:
                if not str(self.x)+" "+str(self.y) in self.visited:
                    self.visited.append(str(self.x)+" "+str(self.y))

    def nextTo(self, pos2) -> bool:
        return (abs(self.x - pos2.x) <= 1) and (abs(self.y - pos2.y) <= 1)

try:
    f=open(str(Path(__file__).resolve().parent)+"/"+nom_fich+".txt")
    choix = int(input("Choisissez sur quelle partie tester la solution (1 ou 2): "))
    if choix < 1 or choix > 2:
        raise ValueError
    ####################################################
    if choix == 1:
        tete, queue = Position(), Position()
        queue.countVisits = True
        for line in f:
            dir, steps = line.split()
            steps=int(steps)
            if dir == "R":
                tete.x+=steps
            elif dir == "L":
                tete.x-=steps
            elif dir == "U":
                tete.y+=steps
            else:
                tete.y-=steps
            queue.moveTo(tete)
        print(len(queue.visited))
    else:
        # rope[0]: tete
        # rope[9]: queue
        rope = [Position() for i in range(10)]
        rope[-1].countVisits = True
        for line in f:
            dir, steps = line.split()
            steps=int(steps)
            if dir == "R":
                rope[0].x+=steps
            elif dir == "L":
                rope[0].x-=steps
            elif dir == "U":
                rope[0].y+=steps
            else:
                rope[0].y-=steps
            for i in range(9):
                rope[i+1].moveTo(rope[i])
            # print(rope[-1])
        print(len(rope[-1].visited))
    ####################################################
except FileNotFoundError:
    if nom_fich == "i" or nom_fich == "it":
        print(f"Vous n'êtes pas dans le bon répertoire !")
    else:
        print(f"'{nom_fich}' n'est pas un nom de fichier correct (noms attendus: i ou it)")
except ValueError:
    print(f"'{choix}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")