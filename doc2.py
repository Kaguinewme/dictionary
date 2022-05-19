# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a="w3resource"
count={"w":0,3:0,"r":0,"e":0,"s":0,"o":0,"u":0,"c":0}
for i in a:
    if i=="w":
        count["w"]+=1
    elif i=="3":
        count[3]+=1
    elif i=="r":
        count["r"]+=1
    elif i=="e":
        count["e"]+=1
    elif i=="s":
        count["s"]+=1
    elif i=="o":
        count["o"]+=1
    elif i=="u":
        count["u"]+=1
    elif i=="c":
        count["c"]+=1
print(count)

        