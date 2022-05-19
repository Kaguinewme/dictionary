# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI"
# to a dictionary, were the letters are the keys and their frequencies are the values.

# word = "MISSISSIPPI"
# count = {"M":0,"I":0,"S":0,"P":0}
# for i in word:
#     if i=="M":
#         count["M"]+=1
#     elif i=="I":
#         count["I"]+=1
#     elif i=="S":
#         count["S"]+=1
#     elif i=="P":
#         count["P"]+=1
# print(count)

# word = "MISSISSIPPI"
# i=0
# a={}
# while i<len(word):
#     j=0
#     count=0
#     while j<len(word):
#         if word[i]==word[j]:
#             count+=1
#         j+=1
#     a.update({word[i]:count})
#     i+=1
# print(a) 



# d="missisippi"
d=[1,2,1,2,3,4,3,4,5,6,5,6,8]
a=[]
for i in d:
  if i in a:
    a[i]+=1
  else:
    a[i]=1
print(a)
     