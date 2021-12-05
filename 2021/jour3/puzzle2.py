import copy
T=[]
with open('i') as f:
    for line in f:
        T.append(line.replace("\n",""))
TT=copy.deepcopy(T)

cpt1=0;cpt0=0
for i in range(len(T)):
    if T[i][0]=='1':
        cpt1+=1
    else:
        cpt0+=1
if cpt1<cpt0:
    dom='0'
else:
    dom='1'
nvT=[]
for i in T:
    if i[0]==dom:
        nvT.append(i)
j=1
while j<len(T[0]) and len(nvT)!=1:
    cpt1=0;cpt0=0
    for i in range(len(nvT)):
        if nvT[i][j]=='1':
            cpt1+=1
        else:
            cpt0+=1
    if cpt1<cpt0:
        dom='0'
    else:
        dom='1'
    T=copy.deepcopy(nvT)
    nvT=[]
    for i in T:
        if i[j]==dom:
            nvT.append(i)
    j+=1

oxygen_r=int(nvT[0],2)
T=copy.deepcopy(TT)

cpt1=0;cpt0=0
for i in range(len(T)):
    if T[i][0]=='1':
        cpt1+=1
    else:
        cpt0+=1
if cpt1<cpt0:
    dom='0'
else:
    dom='1'
nvT=[]
for i in T:
    if i[0]!=dom:
        nvT.append(i)
j=1
while j<len(T[0]) and len(nvT)!=1:
    cpt1=0;cpt0=0
    for i in range(len(nvT)):
        if nvT[i][j]=='1':
            cpt1+=1
        else:
            cpt0+=1
    if cpt1<cpt0:
        dom='0'
    else:
        dom='1'
    T=copy.deepcopy(nvT)
    nvT=[]
    for i in T:
        if i[j]!=dom:
            nvT.append(i)
    j+=1
CO2_s=int(nvT[0],2)

print(CO2_s,oxygen_r,CO2_s*oxygen_r)