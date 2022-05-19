def length():
    dict1={"q":3,"r":[2,3,4,5],"t":"kagui","y":"v","o":[1,2,3]}
    # dict1 = {'a':[1, 2, 3],'b':[1, 2, 3],'c':5,'d':"nopqrs",'e':["A", "B", "C"]}
    count = 0 
    for i in dict1:
        if isinstance(dict1[i], int):
            count += 1
        elif isinstance(dict1[i], str):
            count += 1
        else:
            count += len(dict1[i])
    print("The total length of value is:", count)
if __name__ == '__main__':
    length()
