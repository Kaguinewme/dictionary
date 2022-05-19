# Write a program to remove duplicate keys.
dict1={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# print(dict1)
a=[]
b={}
for val, key in dict1.items():
    if key not in a:
        a.append(key)
        b[val]=key
print(b)   