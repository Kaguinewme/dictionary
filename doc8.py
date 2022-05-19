# Write a Python program to check whether a given key already exists in a dictionary.
d={1:"a",2:"b", 3:"c",4:"d",5:"e"}
def key(a):
    if a in d:
        print("exist")
    else:
        print("not exist")
a=int(input("enter the key"))
key(a)

        