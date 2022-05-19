# Write a program to sort a dictionary in ascending or descending according to its values .


# dict={"bijender":45,"deepak":60,"param":20,"anjali":30,"roshini":50}
# a=[]
# for i  in dict:
#       # for j in dict:
#         a.append(dict[i])
#         # a.sort()
#         a.sort(reverse=True)
# print(a)

# name={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# s=sorted(name.values())
# dict={}
# dic={}
# for i in s:
#     for j in name.keys():
#         if name[j]==i:
#             dict[j]=name[j]
# for i in reversed(s):
#     for j in reversed (name.keys()):
#         if name[j]==i:
#             dic[j]=name[j]
# print(dict)
# print(dic)

dic={"bijender":45,"deepak":60,"param":20,"anjali":30,"roshini":50}
a,b,c,d,e=0,0,0,0,0
s=[]
for i in dic:
  for j in dic:
      if dic[j]>a:
        a=dic[j]
        f=j
      elif dic[j]>b and dic[j]<a:
         b=dic[j]
         g=j
      elif dic[j]>c and dic[j]<b:
        c=dic[j]
        h=j
      elif dic[j]>d and dic[j]<c:
        d=dic[j]
        l=j
      elif dic[j]>e and dic[j]<d:
        e=dic[j]
        m=j 
p=f,a,g,b,h,c,l,d,m,e
print(p)
