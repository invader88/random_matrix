from random_matrix import random_m
f = random_m(10)

for i in range(0, len(f)):
    
        f[i][i] = 0
for i in range(0, len(f)):
    print(f[i])
