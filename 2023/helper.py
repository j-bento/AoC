def read_input(file_path, choice=1):
    try:
        if choice < 1 or choice > 2:
            raise ValueError
        if choice == 1:
            file_path += "/i.txt"
        else:
            file_path += "/it.txt"
        return open(file_path, "r")
    except FileNotFoundError:
        print(f"'{file_path}' n'est pas un chemin valide")
    except ValueError:
        print(f"'{choice}' n'est pas une valeur correcte (valeurs attendues: 1 ou 2)")
    
class Choice:
    REAL = 1
    TEST = 2