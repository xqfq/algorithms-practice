# -*- coding: utf-8 -*-

from mergeSort import *
def mergeSort_test():
    s = []
    assert mergeSortTD(s) == [], 'empty sequence case fails'
    s = [1]
    assert mergeSortTD(s) == [1], 'single element case fails'
    s = [1,2,3,4,5,6]
    assert mergeSortTD(s) == s, 'pre-sorted sequence case fails'
    s.reverse()
    assert mergeSortTD(s) == [1,2,3,4,5,6], 'reversed sequence case fails'
    s = [1,5,2,6,3,7,4]
    assert mergeSortTD(s) == [1,2,3,4,5,6,7], 'even # ele case fails'
    s = [1,5,2,6,3,7,4,7]
    assert mergeSortTD(s) == [1,2,3,4,5,6,7,7], 'odd # ele case fails'
    print('MergeSortTD fucntion works.')
    
    s = []
    assert mergeSortBU(s) == [], 'empty sequence case fails'
    s = [1]
    assert mergeSortBU(s) == [1], 'single element case fails'
    s = [1,2,3,4,5,6]
    assert mergeSortBU(s) == s, 'pre-sorted sequence case fails'
    s.reverse()
    assert mergeSortBU(s) == [1,2,3,4,5,6], 'reversed sequence case fails'
    s = [1,5,2,6,3,7,4]
    assert mergeSortBU(s) == [1,2,3,4,5,6,7], 'even # ele case fails'
    s = [1,5,2,6,3,7,4,7]
    assert mergeSortBU(s) == [1,2,3,4,5,6,7,7], 'odd # ele case fails'
    print('MergeSortBU fucntion works.')
mergeSort_test()
