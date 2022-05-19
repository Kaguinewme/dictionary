# # Write a program such that the below given dictionaries are into a single dictionary 
# # and add the values having same key.
dict1={1:10, 2:20}
dict2={3:30,2:40}
dict3={5:50,6:60}
for i in dict1:
    if i in dict2:
        dict2[i]=dict1[i]+dict2[i]
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
# a={**dict1,**dict2,**dict3}
# print(a)
  


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = dict(d1) 
# d3.update(d2) 
# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)



#\



