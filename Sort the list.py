import random
import time


def InsertionSort(A):
    for i in range(1, len(A)):
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j -= 1
            A[j + 1] = current
    return A


def MERGE(L, R):
    i, j = 0, 0
    lst = []
    while i < len(L) or j < len(R):
        try:
            if L[i] <= R[j]:
                lst.append(L[i])
                i += 1
            else:
                lst.append(R[j])
                j += 1

        except:
            if i == len(L):
                while j < len(R):
                    lst.append(R[j])
                    j += 1
            else:
                while i < len(L):
                    lst.append(L[i])
                    i += 1
    return lst


def MERGESORT(A):
    n = len(A)
    if n <= 1:
        return A

    L = MERGESORT(A[0: int(n / 2)])
    R = MERGESORT(A[int(n / 2):])
    return MERGE(L, R)


def main():
    size_of_list = 10000
    max_of_list = 15000
    initial_list = random.sample(range(0, max_of_list), size_of_list)
    print("initial list:", initial_list)
    print("please wait for sort!!!")

    t1_start = time.time()
    InsertionSort(initial_list)
    t1_stop = time.time()

    t2_start = time.time()
    MERGESORT(initial_list)
    t2_stop = time.time()


main()
