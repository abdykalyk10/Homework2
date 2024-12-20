def bubble_sort(list_n):
    for i in range(len(list_n) - 1):
        for n in range(len(list_n) - 1 - i):
            if list_n[n] > list_n[n + 1]:
                list_n[n], list_n[n + 1] = list_n[n + 1], list_n[n]
    return list_n

n= bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(n)

def binary_sarch(A,Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    pos = -1
    while First <= Last:
        Middle = (First + Last) // 2
        if Val == A[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            pos = Middle
            break
        elif Val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1
    if ResultOk == True:
        print("Элемент найден на позиции: ", pos)
    else:
        print("Элемент не найден")

binary_sarch([1, 2, 3], 1)