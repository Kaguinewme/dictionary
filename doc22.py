#  Write a Python program to create and display all combinations of letters, selecting 
#  each letter from a different key in a dictionary.
# Expected Output:
# ac
# ad
# bc
# bd
              
dic= {'1':['a', 'b',], '2':['c', 'd']}
a=list(dic.values())
for i in a[0]:
    for j in a[1]:
        print(i+j)
