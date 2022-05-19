# def dict(string):
#     a={}
#     for i in string:
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
#     for j in  range (len(string)):
#         if a[string[j]]==1:
#             return string[j],j 
# string=input("enter")
# print(dict(string))


string=input("enter")
a={}
for i in string:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
for j in  range (len(string)):
    if a[string[j]]==1:
        print(string[j],j)
        break
