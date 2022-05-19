# Write a Python program to convert a list into a nested dictionary of keys.
dic=[1, 2, 3,4,5]
a={}
b={}
new=a=b={}
for i in dic:
    b[i]={}
    b=b[i]
print(new)
