# Write a program to print 'exists' if entered key already exists in the dictionary 
# and print 'not exists' if the entered key does not exist.

dict={"name":"raju","marks":56}
def key(a):
    if a in dict:
        print("exist")
    else:
        print("not exist")
a=input("enter the key:")
key(a)
        