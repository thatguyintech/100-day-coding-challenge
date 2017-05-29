import heapq

def efficientSortIdea(arr, k):
    return sorted(arr)[k-1]

def minHeapIdea(arr, k):
    heapq.heapify(arr)
    last = arr[0]
    while k > 0:
        last = heapq.heappop(arr)
        k -= 1
    return last

def maxHeapIdea(arr, k):
    # negate values when adding into python's min-heap implementation
    arr = map(lambda x: -x, arr)
    h = arr[:k]
    heapq.heapify(h)
    for num in arr[k:]:
        heapq.heappushpop(h, num)
    return -heapq.heappop(h)

def testEfficientSortIdea():
    assert efficientSortIdea([1, 2, 3, 4, 5], 3) == 3
    assert efficientSortIdea([3, 1, 4, 2, 5], 3) == 3
    assert efficientSortIdea([5, 4, 3, 2, 1], 3) == 3
    assert efficientSortIdea([4, 2], 1) == 2
    assert efficientSortIdea([1, 9, 2, 7, 4, 6, 4, 2, 1, -1, -5, -9], 5) == 1
    assert efficientSortIdea([-3, -6, 1, 0, 1], 4) == 1

def testMinHeapIdea():
    assert minHeapIdea([1, 2, 3, 4, 5], 3) == 3
    assert minHeapIdea([3, 1, 4, 2, 5], 3) == 3
    assert minHeapIdea([5, 4, 3, 2, 1], 3) == 3
    assert minHeapIdea([4, 2], 1) == 2
    assert minHeapIdea([1, 9, 2, 7, 4, 6, 4, 2, 1, -1, -5, -9], 5) == 1
    assert minHeapIdea([-3, -6, 1, 0, 1], 4) == 1

def testMaxHeapIdea():
    assert maxHeapIdea([1, 2, 3, 4, 5], 3) == 3
    assert maxHeapIdea([3, 1, 4, 2, 5], 3) == 3
    assert maxHeapIdea([5, 4, 3, 2, 1], 3) == 3
    assert maxHeapIdea([4, 2], 1) == 2
    assert maxHeapIdea([1, 9, 2, 7, 4, 6, 4, 2, 1, -1, -5, -9], 5) == 1
    assert maxHeapIdea([-3, -6, 1, 0, 1], 4) == 1

def tests():
    testEfficientSortIdea()
    testMinHeapIdea()
    testMaxHeapIdea()

if __name__ == "__main__":
    tests()
