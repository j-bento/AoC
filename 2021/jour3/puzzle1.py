T=[]
with open('it') as f:
    for line in f:
        T.append(line.replace("\n",""))
gamma=''
for j in range(len(T[0])):
    cpt1=0;cpt0=0
    for i in range(len(T)):
        if T[i][j]=='1':
            cpt1+=1
        else:
            cpt0+=1
    if cpt0<cpt1:
        gamma+='1'
    else:
        gamma+='0'
    print(cpt0,cpt1)
epsilon=''
for i in ['1' if char=='0' else '0' for char in gamma]:
    epsilon+=i
print(int(gamma,2),int(epsilon,2))
print(int(gamma,2)*int(epsilon,2))