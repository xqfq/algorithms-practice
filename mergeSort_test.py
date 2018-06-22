# -*- coding: utf-8 -*-

from mergeSort import *
def mergeSort_test():
    s = []
    assert mergeSort(s) == [], 'empty sequence case fails'
    s = [1]
    assert mergeSort(s) == [1], 'single element case fails'
    s = [1,2,3,4,5,6]
    assert mergeSort(s) == s, 'pre-sorted sequence case fails'
    s.reverse()
    assert mergeSort(s) == [1,2,3,4,5,6], 'reversed sequence case fails'
    s = [1,5,2,6,3,7,4]
    assert mergeSort(s) == [1,2,3,4,5,6,7], 'even # ele case fails'
    s = [1,5,2,6,3,7,4,7]
    assert mergeSort(s) == [1,2,3,4,5,6,7,7], 'odd # ele case fails'
    print('MergeSort fucntion works.')
mergeSort_test()