import heapq

def outofplace(arr):
    heapq.heapify(arr)
    result = []
    size = len(arr)
    while size > 0:
        result.append(heapq.heappop(arr))
        size -= 1
    return result

def inplace(arr):
    print arr

def testHeapsort():
    assert outofplace([1]) == [1]
    assert outofplace([2,1]) == [1,2]
    assert outofplace([1,6,4]) == [1,4,6]
    assert outofplace([-1,6,4]) == [-1,4,6]
    assert outofplace([3,3,3,8,1,6,9,-3,-5,-19]) == [-19,-5,-3,1,3,3,3,6,8,9]

    t1, o1 = [1], [1] 
    inplace(t1)
    assert t1 == o1

    t2, o2 = [2, 1], [1, 2] 
    inplace(t2)
    assert t2 == o2

    t3, o3 = [1,6,4], [1,4,6] 
    inplace(t3)
    assert t3 == o3

    t4, o4 = [-1,6,4], [-1,4,6] 
    inplace(t4)
    assert t4 == o4

    t5, o5 = [3,3,3,8,1,6,9,-3,-5,-19], [-19,-5,-3,1,3,3,3,6,8,9] 
    inplace(t5)
    assert t5 == o5

def tests():
    testHeapsort()

if __name__ == "__main__":
    tests()
