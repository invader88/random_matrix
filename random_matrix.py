import random
n = int(input("Enter dimension of matrix: "))
def random_m(a):
    b = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(n):
            b[i][j] = random.randint(100,999)
        print('{}'.format(b[i],[j]))
random_m(n)
