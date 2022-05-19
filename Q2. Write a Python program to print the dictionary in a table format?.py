dict ={}
dict1 = {1: ["Sam", 21, 'python'],
     2: ["Rim", 20, 'jsnode'],
     3: ["Lem", 22, ' java'],
     }
print ("{:<8} {:<8} {:<8}".format('Name', 'Age', 'Course'))
for key, value in dict1.items():
    name, age, course = value
    print("{:<8} {:<8}{:<8}".format(name,age, course))
  