# Write a program to print the top 3 highest key of a given dictionary.
dic = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
x=0
y=0
z=0
d=[]
for i in dic:
      for j in dic:
       if dic[j]>x:
         x=dic[j]
         a=j
       elif dic[j]>y and dic[j]<x:
         y=dic[j]
         b=j
       elif dic[j]>z and dic[j]<y:
        z=dic[j]
        c=j
d.append(a)
d.append(b)
d.append(c)
print(d)

