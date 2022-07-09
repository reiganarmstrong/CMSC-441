
import copy
import math
import random
import time

# Insertion sort


def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

# merge sort


def Merge_Sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        Merge(A, p, q, r)

# merge


def Merge(A, p, q, r):
    n_1 = q-p+1
    n_2 = r-q
    left = []
    right = []
    for i in range(n_1):
        left.append(A[p+i])
    for j in range(n_2):
        right.append(A[q+j+1])
    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i = i+1
        else:
            A[k] = right[j]
            j = j+1

# checks how long it takes for insertion sort to sort a list


def insertion_sort_test(Unsorted_List):
    before = time.time()
    Insertion_Sort(Unsorted_List)
    after = time.time()
    return after-before

# appends a list of random numbers


def append_list(list_of_lists):
    length_of_list = len(list_of_lists)
    list_of_lists.append([])
    for i in range(length_of_list, -1, -1):
        list_of_lists[length_of_list].append(random.randint(1, 100))

# checks the time it takes to sort the list


def merge_sort_test(Unsorted_List):
    before = time.time()
    Merge_Sort(Unsorted_List, 0, len(Unsorted_List)-1)
    after = time.time()
    return after-before

# checks that the sorts actually sort


def check_sorts_work():
    Two_D_List = []
    num_lists = 10
    for i in range(num_lists):
        append_list(Two_D_List)
    Two_D_List_2 = copy.deepcopy(Two_D_List)
    for i in range(10):
        print(f"before sorting: {Two_D_List[i]}")
        Merge_Sort(Two_D_List[i], 0, len(Two_D_List[i])-1)
        print(f"after merge-sort: {Two_D_List[i]}")
        Insertion_Sort(Two_D_List_2[i])
        print(f"after merge-sort: {Two_D_List_2[i]}\n\n")


if __name__ == "__main__":
    # checks that the sorts do sort correctly
    check_sorts_work()
    # takes an average of 100000 calculated crossovers
    num_to_avg = 100000
    avg_crossover = 0
    # accounts for when crossover is a value greater than 100
    num_failed_to_crosover = 0
    for z in range(num_to_avg):
        Two_D_List = []
        num_lists = 100
        for i in range(num_lists):
            append_list(Two_D_List)
        # creates a deep copy of Two_D_List
        Two_D_List_2 = copy.deepcopy(Two_D_List)
        crossover_found = False
        i = 0
        crossover = 0
        while(i < num_lists and not crossover_found):
            merge_time = merge_sort_test(Two_D_List[i])
            insertion_time = insertion_sort_test(Two_D_List_2[i])
            if(merge_time < insertion_time):
                crossover_found = True
                crossover = i+1
            i += 1
        if crossover == 0:
            num_failed_to_crosover += 1
        else:
            avg_crossover += crossover
    # calculates the avgcrossover while taking into account the crossovers above 100
    avg_crossover /= num_to_avg-num_failed_to_crosover
    print(f"num crossovers found:{num_to_avg-num_failed_to_crosover}")
    print(avg_crossover)
