def insertionSort(sequence):
    '''
    Sort a sequence of objects in ascending order through insertion sort
    '''
    if len(sequence) <= 1:
        return sequence
    for i in range(len(sequence)):
        val = sequence[i]
        while i-1 >= 0 and sequence[i-1] > val:
            # swap if the ith element is smaller than the element before it
            sequence[i] = sequence[i-1]
            sequence[i-1] = val
            # iterate this process by decrementing i
            i -= 1
    return sequence
