dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}
print("Given Dictionary :", dictA)
k_v_exchanged = {}
for key, value in dictA.items():
   if value not in k_v_exchanged:
      k_v_exchanged[value] = [key]
   else:
      k_v_exchanged[value].append(key)
print("New Dictionary:", k_v_exchanged)