# Q16.Write a Python program to map two lists into a dictionary.
x = ['mango', 'pear', 'apple','papaya']
y= [90, 78, 110, 60]
a=zip(x,y)
b={}
for i, j in a:
    if i not in b:
        b[i]=j
    else:
       pass
print(b)

    
