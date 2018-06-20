from insertionSort import *

def insertionSort_test():
    s = []
    assert insertionSort(s) == [], 'empty sequence case fails'
    s = [1]
    assert insertionSort(s) == [1], 'single element case fails'
    s = [1,2,3,4,5,6]
    assert insertionSort(s) == s, 'pre-sorted sequence case fails'
    s.reverse()
    assert insertionSort(s) == [1,2,3,4,5,6], 'reversed sequence case fails'
    s = [1,5,2,6,3,7,4]
    assert insertionSort(s) == [1,2,3,4,5,6,7], 'general case fails'
    print('InsertionSort fucntion works.')
insertionSort_test()
