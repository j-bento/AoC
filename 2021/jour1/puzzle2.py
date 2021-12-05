with open('input') as f:
    tabInput=[]
    for line in f:
        tabInput.append(int(line))
cpt=0
sumP=tabInput[0]+tabInput[1]+tabInput[2]
for i in range(1,len(tabInput)-2):
    if sumP<tabInput[i]+tabInput[i+1]+tabInput[i+2]:
        cpt+=1
    sumP=tabInput[i]+tabInput[i+1]+tabInput[i+2]
print(cpt)