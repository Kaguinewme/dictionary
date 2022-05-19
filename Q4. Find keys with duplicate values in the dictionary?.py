# dict={1:"apple", 2:"mango",3:"apple",4:"banana", 5:"grapes",6:"mango"}
# a=[]
# for i in dict.values():
#     if i in a:
#         continue
#     else:
#         a.append(i)
# print(set(a))


dict={1:"apple", 2:"mango",3:"apple",4:"banana", 5:"grapes",6:"mango"}
b=[]
for key in dict:
    b.append(dict[key])
i=0
c=[]
while i<len(b):
    if b[i] not in c:
        c.append(b[i])
    i+=1
print(set(c))  

      


