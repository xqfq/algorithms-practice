def shellSort(sequence):
    '''
    Sort a sequence in ascending order through shellSort w/ h = h*3+1
    '''
    h = 1
    length = len(sequence)
    if length <= 1:
        # trivial case
        return sequence

    while h < length:
        # calculate the largest increment
        h = h*3+1

    while h >= 1:
        # iterate until the smallest increment is reached
        # i is used to keep track of the swapping process
        # j is used to build the h-sort
        i = h
        j = h
        while i < length:
            # sort ith element in the subsequence whose increment = h
            val = sequence[i]
            while i-h >= 0 and sequence[i-h] > val:
                sequence[i] = sequence[i-h]
                sequence[i-h] = val
                i -= h
            j = j + h
            i = j
        h = h//3
    return sequence
