
# from collections import Counter
# a={'a':5, 'b':10, 'c':90}
# b={'a':45, 'b':78,'c':10}
# c={'a':90, 'b':30,'c':10}
# d={}
# x=Counter(a)+Counter(b)+Counter(c)
# print(x)


dict =[{"a":20,"b":30,"c":40},
{"a":10,"b":20,"c":30},
{"a":60, "b":50,"c":90}]
a = {}
for i in dict:
    for j, k in i.items():
        if j not in a:
            a[j] = 0
        a[j] += k
print(a)

