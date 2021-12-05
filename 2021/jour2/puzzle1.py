# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
#2003 980 1962940
with open('input')as f:T=[l.split() for l in f];print(sum([int(l[1])for l in T if'f'in l[0]])*(sum([int(l[1])for l in T if'down'in l[0]])-sum([int(l[1])for l in T if'up'in l[0]])))

# cptD=0;cptH=0
# with open('input') as f:
#     for line in f:    
#         l=line.split()
#         if 'f' in l[0]:
#             cptD+=int(l[1])
#         elif 'd' in l[0]:
#             cptH+=int(l[1])
#         elif 'u' in l[0]:
#             cptH-=int(l[1])
        
# print(cptD,cptH,cptH*cptD)