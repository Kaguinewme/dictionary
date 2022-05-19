dic={'a':[8,4,3,2],'b':[4,3,2,8,9]} 
d={}
a=[]
for i in dic:
    a1=[]
    j=-1
    while j>=-len(dic[i]):
        b=dic[i][j]
        a1.append(b)
        j=j-1 
    a.append(a1)
    for k in a:
        c=k
    d[i]=c
print(d)
    