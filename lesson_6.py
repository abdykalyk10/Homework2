def bubble_sort(list_n):
    for i in range(len(list_n) - 1):
        for n in range(len(list_n) - 1 - i):
            if list_n[n] > list_n[n + 1]:
                list_n[n], list_n[n + 1] = list_n[n + 1], list_n[n]
    return list_n

n= bubble_sort([11, 9, 10, 28])
print(n)

def binary_sarch(A,Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1
    while First <= Last:
        Middle = (First + Last) // 2
        if Val == A[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            Pos = Middle
            break
        elif Val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1
    if ResultOk == True:
        print("Элемент найден на позиции: ", Pos)
    else:
        print("Элемент не найден")

binary_sarch(n, 9)