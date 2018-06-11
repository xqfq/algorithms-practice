
def binarySearch(A,x,lo,hi):
    '''
    Searches for an element x in an array A
    Returns True if there is at least one instance of x in A
    Returns False o/w 
    '''
    if len(A) == 0:
        return False
    elif hi == lo:
        return A[hi] == x
    else:
        mid = (hi + lo) // 2
        if A[mid] == x:
            return True
        elif A[mid] > x:
            return binarySearch(A,x,lo,mid-1)
        else:
            return binarySearch(A,x,mid+1,hi)

def binarySearch_test():
    assert binarySearch([],1,0,0) == 0,'Empty array case fails'
    assert binarySearch([1,2,3],1,0,2) == 1,'Leftmost case fails'
    assert binarySearch([1,2,3],3,0,2) == 1,'Rightmost case fails'
    assert binarySearch([1,2,3],2,0,2) == 1,'middle case fails'
    assert binarySearch([1,2,3],4,0,2) == 0,'0 instandce case fails'
    print('binarySearch works')
binarySearch_test()
