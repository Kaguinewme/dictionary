# Write a Python program to match key values in two dictionaries.
a = {'a': 1, 'c': 3, 'b': 2,'d':8}
b = {'a': 1, 'b': 2,'c':3,'d':6}
for i in a:
  if i in b:
      if a[i] == b[i]:
        print(a[i])
        print(i)
        
        
