# Q15.Write a Python program to remove a key from a dictionary.
d = {'a':1,'b':2,'c':3,'d':4,"e":8}
key=input("Enter the key:")
if key in d:
    del d[key]
else:
    print("key not found")
print(d)
