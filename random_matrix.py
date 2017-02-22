import random

def random_m(a):
    
    b = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            b[i][j] = random.randint(100,999)
        print('{}'.format(b[i],[j]))
    return b
        
if __name__ == '__main__':       
    n = int(input("Enter dimension of matrix: "))
    random_m(n)
