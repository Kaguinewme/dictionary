dict = {'1':'a','2':'a','3':'b','4':'b','5':'c','6':'d'}
a =[] 
for i in dict.values(): 
  if i in a: 
    continue 
  else:
    a.append(i)
print (a)
