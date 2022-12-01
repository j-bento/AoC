with open('input') as f:
    lines = [i.split("\n")[0] for i in (f.readlines())]
    calories=[0]
    for line in lines:
        if line != "":
            calories[len(calories)-1] += (int(line))
        else:
            calories.append(0)
    print(max(calories))