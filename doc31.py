#Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

d= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
a=0
b=0
c=0
k=[]
for i in d:
    for j in d:
        if d[j]>a:
            a=d[j]
            x=j
        elif d[j]>b and d[j]<a:
            b=d[j]
            y=j
        elif d[j]>c and d[j]<b:
            c=d[j]
            z=j
        
print(x,a)
print(y,b)
print(z,c)

