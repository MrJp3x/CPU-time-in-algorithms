# import math
import random
from importlib import import_module
from time import time
from math import floor


sort_the_list = import_module('Sort the list')


class SELECT:
    def __init__(self, A, algorithm_find_pivot=None):
        self.lst = A
        self.pivot = None
        self.L = []
        self.R = []
        self.flag = 0
        self.len_A = len(A)
        self.algorithm = algorithm_find_pivot

    def GetPivotIndex(self, A):
        split_list = []
        lst_middle = []
        size_of_list = 5
        for i in range(0, len(A), size_of_list):
            split_list.append(A[i:i + size_of_list])  # split list into n groups (5 element)

        len_split_list = len(split_list)
        for i in range(len_split_list):
            lst_child = sort_the_list.MERGESORT(split_list[i])  # child list is sorted
            middle = lst_child[int((len(lst_child) / 2))]  # find middle in each child list
            lst_middle.append(middle)

        lst_middle = sort_the_list.MERGESORT(lst_middle)  # sort the list_middle
        p = self.FindElement(lst_middle, floor(len_split_list / 2))  # find middle in lst_middle
        return A.index(p)

    def manager(self, i):
        element = self.FindElement(self.lst, i)
        print(f"index element is: {i} and value:", element)
        # print(f"Number of elements in list L :{len(self.L)} \n\t\t L primary:", self.L)
        print("pivot primary value:", self.pivot)
        # print(f"Number of elements in list R :{len(self.R)} \n\t\t R primary:", self.R)
        return element

    def FindElement(self, A, k):
        if len(A) <= 10:
            A = sort_the_list.MERGESORT(A)
            return A[k]

        if self.algorithm == "random":
            index_p = random.randint(0, len(A) - 1)
        else:
            index_p = self.GetPivotIndex(A)

        L, pivot, R = self.Partition(A, index_p)

        if self.flag == 0 and self.len_A == len(A):
            self.L = L
            self.pivot = pivot
            self.R = R
            self.flag = 1

        if len(L) == k:
            return pivot
        elif len(L) > k:
            return self.FindElement(L, k)
        elif len(L) < k:
            return self.FindElement(R, k - len(L))

    def Partition(self, A, index_p):
        L = []
        R = []
        p = A[index_p]
        for i in range(len(A)):
            if A[i] < p:
                L.append(A[i])
            # elif A[i] > p:
            else:
                R.append(A[i])
        return L, p, R


def GenerateListRandom():
    size_of_list = 50000
    max_of_list = 60000
    initial_list = random.sample(range(0, max_of_list), size_of_list)
    return initial_list


def main(index):
    lst = GenerateListRandom()
    print("please wait for find element!!!")

    s = SELECT(lst, "random")
    t1_start = time()
    s.manager(index)
    t1_stop = time()

    s2 = SELECT(lst)
    t2_start = time()
    s2.manager(index)
    t2_stop = time()


main(15000)
