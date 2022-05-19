
# dic = input('enter a key')
# d={"1":2,"2":5,"3":7,"4":10}
# a={}
# for i in dic:
#     a[i]=d[i]
# print(a)

d={"1":"a","2":"5","3":"7","4":"10"}
a=input("enter")
for i in d:
    if a==d[i]:
        print(i)
    elif a==i:
        print(d[i])