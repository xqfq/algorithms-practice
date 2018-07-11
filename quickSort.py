import random

def partition(sequence,lo,hi):
    pivot_index = lo
    pivot = sequence[lo]
    while True:
        while sequence[hi] >= pivot:
            hi -= 1
            if hi < lo:
                break
        while sequence[lo] <= pivot:
            lo += 1
            if lo > hi:
                break
        if lo >= hi:
            break
        else:
            sequence[lo],sequence[hi] = sequence[hi],sequence[lo]
    sequence[pivot_index],sequence[lo-1] = sequence[lo-1],sequence[pivot_index]
    return lo-1

def quickSort(sequence,lo=0,hi=None,rand = True):
    if rand == True:
        random.shuffle(sequence)
    if hi == None:
        hi = len(sequence)-1
    if hi <= lo:
        return sequence
    i = partition(sequence,lo,hi)
    quickSort(sequence,lo,i-1,False)
    quickSort(sequence,i+1,hi,False)
    return sequence