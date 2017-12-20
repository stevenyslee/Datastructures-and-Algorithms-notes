from math import ceil,floor
from random import randint

def swap (a,f,k):

    a[f],a[k] = a[k],a[f]

def qsort(a:list, start:int, end:int):
    if (start>= end):
        return
    pIndex = partition (a, start, end)
    qsort(a, start, pIndex-1)
    qsort(a, pIndex+1, end)

def partition(a:list,low:int,high:int):

    pivot = a[high]
    part_index = low

    i = low

    while i < high:
        if a[i] < pivot:
            swap(a,i,part_index)
            part_index += 1
        i += 1

    swap(a, i, part_index)

    return part_index


u = list(set([randint(-100000,100000) for x in range(3000)]))
qsort(u, 0, len(u)-1)
assert u == sorted(u)
