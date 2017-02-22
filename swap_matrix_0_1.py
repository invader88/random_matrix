from random_matrix import random_m
f = random_m(10)

for i in range(0, len(f)):
    for j in range(0, len(f)):
        if f[i][j]%2 == 0:
           f[i][j] = 1
        elif f[i][j]%2 != 0:
            f[i][j] = 0
        
        
            
for k in range(0, len(f)):
    print(f[k])
