
# a=int(input("enter key:"))
# x={}
# for i in range(a):
#     b=input("enter:")
#     x[b]={}
#     c=input("enter name:")
#     x[b]["name"]=c
#     d=input("enter age:")
#     x[b]["age"]=d
# print(x)



# dic=[1, 2, 3,4,5]
# a={}
# b={}
# new=a=b={}
# for i in dic:
#     b[i]={}
#     b=b[i]
# print(new)

# a=int(input("enter key:"))
# x={}
# for i in range(a):
#     b=input("enter:")
#     x[b]={}
#     c=input("enter name:")
#     x[b]["name"]=c
#     d=input("enter age:")
#     x[b]["age"]=d
# print(x)


dict1={'1':10,'2':60,'3':30,'5':50,'4':60,'5':3}
dict2 = {}
for i, j in dict1.items():
    dict2[j] = dict2.get(j, []) + [i]
print(dict2)

# dict={'1':10,'2':60,'3':30,'5':50,'4':60,'5':3}
# a = {}
# for i in dict:
#     a.setdefault(dict[i], []).append(i)
# print(a)


