from random_matrix import random_m
f = random_m(10)
f1 = [[0 for i in range(len(f))] for j in range(len(f))]
for h in range(len(f)):
    for t in range(len(f)):
        f1[h][t] = f[t][h]
print(" ")
print("90 degrees rotated matrix below: ")
print(" ")
for v in range(len(f)):
    print(f1[v][::-1])
