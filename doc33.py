#  Print a dictionary line by line
#output
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja
# class : V                                                                                                     
# roll_id : 3 

students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in students:
    print (i)
    for j in students[i]:
        print (j,':',students[i][j])
      
    


