a = eval(input("Enter a list to sort: "))
def my_sort(b):
    for i in range(0, len(b)):
        for j in range(i+1, len(b)):
            if b[i]>b[j]:
                b[i],b[j]=b[j],b[i]
    return b
print(my_sort(a))
