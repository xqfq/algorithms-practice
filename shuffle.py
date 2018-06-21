from random import *
def shuffle(sequence):
    '''
    randomly shuffles a sequence
    '''
    for i in range(len(sequence)):
        val = sequence[i]
        index = randint(0,i)
        sequence[i] = sequence[index]
        sequence[index] = val
    return sequence

