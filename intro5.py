## total sum and print in one dictionary
dict = {}
dict[(1,2,4)] = 8
dict[(4,2,1)] = 10
dict[(1,2)] = 12
sum = 0
for k in dict:
  sum += dict[k]
print(sum)
print(dict)