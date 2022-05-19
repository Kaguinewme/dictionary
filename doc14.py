# Q14.Write a Python program to multiply all the items in a dictionary.
# d={"a":4,"b":2,"c":6,"d":9}
# def pro(d):
#     mul=1
#     for i in d.values():
#         mul*=i
#     return mul
# print(pro(d))


d={"a":4,"b":2,"c":6,"d":9}
sum=0
for i in d.values():
    sum+=i
print(sum)