# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

# d={"a":23, "b":30,"c":90,"d":100,"e":2}
# print(max(d.values()))
# print(min(d.values()))

d={"a":23, "b":30,"c":90,"d":100,"e":2}
a=[]
for i in d.values():
    a.append(i)
print(max(a))
print(min(a))
