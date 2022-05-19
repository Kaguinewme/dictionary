
dict = {1 : "a", 2 : "b", 3: "c",4:"d"}
key = []
value = []
for i in dict.items():
    key.append(i[0])
    value.append(i[1])
print ("keys : ", str(key))
print ("values : ", str(value))