dict = [{'a': 30, 'b': 29}, {'c': 31, 'd': 46,}, {'e': 32}]
maxv = 0
for i in dict:
    if max(i.values()) > maxv:
        maxv = max(i.values())
print(maxv)
        