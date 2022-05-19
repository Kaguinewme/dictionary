
a=input("enter :")
b=input("enter:")
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
d={}
for i in b:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
print(c)
print(d)
if c==d:
      print(True)
else:
      print(False)



