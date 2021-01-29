from heapq import *

def sortKSortedArray(arr, k):
    heap = arr[:k]
    heapify(heap)

    remaining = arr[k:]

    result = []
    for num in remaining:
        # push num into the heap to maintain k+1 elements,
        # then pop the min
        result.append(heappushpop(heap, num))

    while len(heap) > 0:
        result.append(heappop(heap))

    return result

def testSortKSortedArray():
    assert sortKSortedArray([1,4,5,2,3,7,8,6,10,9], 2) == [1,2,3,4,5,6,7,8,9,10]
    assert sortKSortedArray([2,1,3], 1) == [1, 2, 3]

def tests():
    testSortKSortedArray()

if __name__ == "__main__":
    tests()
