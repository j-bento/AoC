with open('input') as f:
    lines = [i.split("\n")[0] for i in (f.readlines())]
    calories=[0]
    for line in lines:
        if line != "":
            calories[len(calories)-1] += (int(line))
        else:
            calories.append(0)
    elf1 = calories.pop(calories.index(max(calories)))
    elf2 = calories.pop(calories.index(max(calories)))
    elf3 = calories.pop(calories.index(max(calories)))
    print(elf1+elf2+elf3)