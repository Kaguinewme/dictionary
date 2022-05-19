
ages = {'Mat': 30,'Kati': 29,'Nik': 31,'Jack': 43,'Jill': 43,'Ali': 32,'Ken': 43}
max_keys = [key for key, value in ages.items() 
if value == max(ages.values())]
print(max_keys)