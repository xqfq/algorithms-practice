# -*- coding: utf-8 -*-

def merge(s1,s2):
    '''
    merge two sorted lists and produce a sorted list
    '''
    length = len(s1) + len(s2)
    result = [0] * length
    index1 = 0
    index2 = 0
    for i in range(length):
        # build the result
        if index1 >= len(s1):
            # when all ele from s1 have been sorted, append the remaining ele
            result[i] = s2[index2]
            index2 += 1
        elif index2 >= len(s2):
            # when all ele from s2 have been sorted, append the remaining ele
            result[i] = s1[index1]
            index1 += 1
        else:            
            if s1[index1] <= s2[index2]:
                # put the ele from s1 before the ele from s2 
                # if the former is at most as large as the latter
                result[i] = s1[index1]
                index1 += 1
            else:
                # else put the ele from s2 first
                result[i] = s2[index2]
                index2 += 1
    return result

def mergeSortTD(sequence):
    '''
    sort a sequence using merge sort algorithm
    '''
    if len(sequence) <=1:
        # base case
        return sequence
    else:
        # sort by sorting and merging the subsequences recursively
        left = mergeSortTD(sequence[0:len(sequence)//2])
        right = mergeSortTD(sequence[len(sequence)//2:])
        return merge(left,right)

def mergeSortBU(sequence):
    size = 1
    while size < len(sequence):
        low = 0
        while low < len(sequence):
            sequence[low:min(low+2*size,len(sequence))] = merge(sequence[low:low+size],sequence[low+size:min(low+2*size,len(sequence))])
            low += 2 * size
        size = size * 2
    return sequence

        
    
        

