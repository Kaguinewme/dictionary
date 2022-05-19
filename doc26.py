# Write a Python program to print a dictionary in table format
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11


# dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# a={}
# print("{:<3} {:<3} {:<3}".format("C1","C2","C3"))
# for i, j in dict.items():
#     C1,C2,C3=j
#     print("{:<3} {:<3} {:<3}".format(C1,C2,C3))

dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value)
    for key, value in dict.items())):
    print(*row)


   

