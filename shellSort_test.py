from shellSort import *

def shellSort_test():
    s = []
    assert shellSort(s) == [], 'empty sequence case fails'
    s = [1]
    assert shellSort(s) == [1], 'single element case fails'
    s = [1,2,3,4,5,6]
    assert shellSort(s) == s, 'pre-sorted sequence case fails'
    s.reverse()
    assert shellSort(s) == [1,2,3,4,5,6], 'reversed sequence case fails'
    s = [1,5,2,6,3,7,4]
    assert shellSort(s) == [1,2,3,4,5,6,7], 'general case fails'
    print('ShellSort fucntion works.')
shellSort_test()
