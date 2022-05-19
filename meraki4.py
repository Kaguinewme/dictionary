# Write a program remove the first key value pair from a nested dictionary.
dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME', 'B' : 'To','C' : 'DHARAMSALA'}}
a=dic[3]
# n_dic.pop("A")
for i,j in dic.items():
    del dic[3]["A"]
    break
print(dic)

# a={"savita":"himachal","kagui":"manipur"}
# for i in a:
#     print(a[i])
