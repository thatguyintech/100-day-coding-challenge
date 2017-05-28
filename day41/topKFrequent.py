## A sample heap data structure ##
from collections import deque

class MaxHeap:
    def __init__(self, arr=[]):
        self.heap = deque()
        self.size = 0
        if len(arr) > 0:
            self.size = len(arr)
            self.heapify(arr)

    # runtime: O(logn) aka the height of the heap
    def getMax(self):
        if self.size > 0:
            ret = self.heap.popleft()
            self.size -= 1
            if self.size > 0:
                self.heap.appendleft(self.heap.pop())
                self.bubbleDown(0)
            return ret

    # runtime: O(1) 
    def peek(self):
        if self.size > 0:
            return self.heap[0]

    # runtime: O(logn) aka the height of the heap
    def push(self, val):
        self.size += 1
        self.heap.append(val)
        self.bubbleUp()

    # runtime: O(nlogn)
    def heapify(self, arr):
        self.heap = deque(arr)
        for i in xrange(self.size-1, -1, -1):
            self.bubbleDown(i)

    # runtime: O(1)
    def isEmpty(self):
        return self.size == 0

    def bubbleDown(self, index):
        if self.size > 0:
            i = index
            h = self.heap
            withinBounds = 2*i + 2 < self.size
            while withinBounds and (h[i][1] < h[2*i + 1][1] or h[i][1] < h[2*i + 2][1]):
                if h[i][1] < h[2*i + 1][1] and h[i][1] < h[2*i + 2][1]:
                    if h[2*i + 1][1] > h[2*i + 2][1]:
                        h[i], h[2*i + 1] = h[2*i + 1], h[i]
                        i = 2*i + 1
                    else:
                        h[i], h[2*i + 2] = h[2*i + 2], h[i]
                        i = 2*i + 2
                elif h[i][1] < h[2*i + 1][1]:
                    h[i], h[2*i + 1] = h[2*i + 1], h[i]
                    i = 2*i + 1
                elif h[i][1] < h[2*i + 2][1]:
                    h[i], h[2*i + 2] = h[2*i + 2], h[i]
                    i = 2*i + 2
                withinBounds = 2*i + 2 < self.size

            if 2*i + 1 < self.size and h[i][1] < h[2*i + 1][1]:
                h[i], h[2*i + 1] = h[2*i + 1], h[i]
            elif 2*i + 2 < self.size and h[i][1] < h[2*i + 2][1]:
                h[i], h[2*i + 2] = h[2*i + 2], h[i]

    def bubbleUp(self):
        if self.size > 0:
            i = self.size-1
            h = self.heap
            withinBounds = i/2 >= 0
            while withinBounds and (h[i] > h[i/2]):
                h[i/2], h[i] = h[i], h[i/2]
                i /= 2
                withinBounds = i/2 >= 0

from collections import Counter

def topKFrequent(nums, k):
    freqs = Counter(nums)
    h = MaxHeap(freqs.items())
    ret = list()
    while k > 0:
        ret.append(h.getMax()[0])
        k -=1
    return ret

def testTopKFrequent():
    assert set(topKFrequent([], 0)) == set([])
    assert set(topKFrequent([1], 1)) == set([1])
    assert set(topKFrequent([-1, -1], 1)) == set([-1])
    assert set(topKFrequent([1,1,1,2,2,3], 2)) == set([1, 2])
    assert set(topKFrequent([-1,-1,-1,2,2,3], 2)) == set([-1, 2])
    assert set(topKFrequent([1,1,1,2,2,3], 3)) == set([1, 2, 3])
    assert set(topKFrequent([1,1,1,2,2,2,3,3,3], 3)) == set([1, 2, 3])
    assert set(topKFrequent([4,1,-1,2,-1,2,3], 2)) == set([-1, 2])
    assert set(topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10)) == set([1,2,5,3,7,6,4,8,10,11])

def main():
    testTopKFrequent()

if __name__ == "__main__":
    main()
