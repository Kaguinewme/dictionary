# Write a program to print the top 3 highest values of a given dictionary.

# dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# a,b,c=0,0,0
# k=[]
# for i in  dict:
#     for j in dict:
#      if dict[j]>a:
#         a=dict[j]
#      elif dict[j]>b and dict[j]<a:
#         b=dict[j]
#      elif dict[j]>c and dict[j]<b:
#         c=dict[j]

# k.append(a)
# k.append(b)
# k.append(c)
# print(k)

dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
b=[]
for i in dict:
   if dict[i]>50:
      a=dict[i]
      b.append(a)
print(b)