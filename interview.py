
dic = input('enter a key')
d={"1":2,"2":5,"3":7,"4":10}
a={}
for i in dic:
    if dic in d:
      a[i]=d[i]
      print(a)
    else:
        print("the key is not in the dictionary")
        