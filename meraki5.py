# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the
# elements of the 2nd list are the corresponding values.

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# def test(list1, list2):
#       return dict(zip(list1, list2))     
# print(test(list1, list2))


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
dic = {}
for i in range(len(list1)):
    # dic[list1[i]] = list2[i]
    dic[list2[i]]=list1[i]
print(dic)

