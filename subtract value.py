
d={"a":10,"b":5,"c":20,"d":4}
a=input("enter:")
b=input("enter:")
for i in d:
    x={}
    if a==i and b==i:
        x=d[a]-d[b]
print(x)
 