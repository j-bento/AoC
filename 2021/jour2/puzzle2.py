cptD=0;cptH=0;aim=0
with open('input') as f:
    for line in f:    
        l=line.split()
        if 'forward' in l[0]:
            cptH+=int(l[1])
            if aim!=0:
                cptD+=(int(l[1])*aim)
        elif 'down' in l[0]:
            aim+=int(l[1])
        elif 'up' in l[0]:
            aim-=int(l[1])
        
print(cptD,cptH,cptH*cptD)