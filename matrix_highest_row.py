from random_matrix import random_m
f = random_m(10)
max_index = f[0]
max_value = sum(f[0])
for i in range(0, len(f)):
    if sum(f[i])>sum(f[0]):
        max_index = f[i]
print("\n", "The row with the highest sum is below: ", "\n", sep="")
print(max_index)
