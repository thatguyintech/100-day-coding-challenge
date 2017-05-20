from collections import deque

class MinHeap:
    def __init__(self, arr=[]):
        self.heap = deque()
        self.size = 0
        if len(arr) > 0:
            self.size = len(arr)
            self.heapify(arr)

    # runtime: O(logn) aka the height of the heap
    def getMin(self):
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
            while withinBounds and (h[i] > h[2*i + 1] or h[i] > h[2*i + 2]):
                if h[i] > h[2*i + 1] and h[i] > h[2*i + 2]:
                    if h[2*i + 1] < h[2*i + 2]:
                        h[i], h[2*i + 1] = h[2*i + 1], h[i]
                        i = 2*i + 1
                    else:
                        h[i], h[2*i + 2] = h[2*i + 2], h[i]
                        i = 2*i + 2
                elif h[i] > h[2*i + 1]:
                    h[i], h[2*i + 1] = h[2*i + 1], h[i]
                    i = 2*i + 1
                elif h[i] > h[2*i + 2]:
                    h[i], h[2*i + 2] = h[2*i + 2], h[i]
                    i = 2*i + 2
                withinBounds = 2*i + 2 < self.size

            if 2*i + 1 < self.size and h[i] > h[2*i + 1]:
                h[i], h[2*i + 1] = h[2*i + 1], h[i]
            elif 2*i + 2 < self.size and h[i] > h[2*i + 2]:
                h[i], h[2*i + 2] = h[2*i + 2], h[i]

    def bubbleUp(self):
        if self.size > 0:
            i = self.size-1
            h = self.heap
            withinBounds = i/2 >= 0
            while withinBounds and (h[i] < h[i/2]):
                h[i/2], h[i] = h[i], h[i/2]
                i /= 2
                withinBounds = i/2 >= 0

def testPush():
    h = MinHeap()
    h.push(2)
    assert h.heap[0] == 2

    h.push(3)
    assert h.heap[0] == 2

    h.push(1)
    assert h.heap[0] == 1

    h.push(5)
    assert h.heap[0] == 1

    h.push(-1)
    assert h.heap[0] == -1

def testHeapify():
    # TODO
    assert True

def testGetMin():
    heap = MinHeap([2, 5, 20])
    assert heap.getMin() == 2
    assert heap.getMin() == 5
    assert heap.getMin() == 20

    heap1 = MinHeap([1, 2, 3, 4, 5])
    assert heap1.getMin() == 1
    assert heap1.getMin() == 2
    assert heap1.getMin() == 3
    assert heap1.getMin() == 4
    assert heap1.getMin() == 5

    heap2 = MinHeap([5, 4, 3, 2, 1])
    assert heap2.getMin() == 1
    assert heap2.getMin() == 2
    assert heap2.getMin() == 3
    assert heap2.getMin() == 4
    assert heap2.getMin() == 5

    heap3 = MinHeap([2, 5, 3, 7, -1])
    assert heap3.getMin() == -1
    assert heap3.getMin() == 2
    assert heap3.getMin() == 3
    assert heap3.getMin() == 5
    assert heap3.getMin() == 7

def testPeek():
    heap = MinHeap([2, 5, 20])
    assert heap.peek() == 2
    assert heap.peek() == 2

    heap1 = MinHeap([1, 2, 3, 4, 5])
    assert heap1.peek() == 1
    assert heap1.peek() == 1

    heap2 = MinHeap([5, 4, 3, 2, 1])
    assert heap2.peek() == 1
    assert heap2.peek() == 1

    heap3 = MinHeap([2, 5, 3, 7, -1])
    assert heap3.peek() == -1
    assert heap3.peek() == -1

def testSize():
    heap = MinHeap()
    assert heap.size == 0

    heap2 = MinHeap([1])
    assert heap2.size == 1

    heap3 = MinHeap([1, 2, 3, 4])
    assert heap3.size == 4

def testIsEmpty():
    heap = MinHeap()
    assert heap.isEmpty()

    heap2 = MinHeap([1])
    assert not heap2.isEmpty()

    heap3 = MinHeap([1, 2, 3])
    assert not heap3.isEmpty()

def testEverything():
    heap = MinHeap([1, 2, 3, 4, -1, -2, -7, 6, -3, -1 , -1])
    assert not heap.isEmpty()
    assert heap.size == 11
    assert heap.peek() == -7
    assert heap.getMin() == -7
    assert heap.getMin() == -3

    heap.push(-10)
    assert heap.peek() == -10
    assert heap.size == 10
    assert heap.getMin() == -10
    assert heap.getMin() == -2
    assert heap.getMin() == -1
    assert heap.getMin() == -1

def tests():
    testPush()
    testHeapify()
    testGetMin()
    testPeek()
    testSize()
    testIsEmpty()
    testEverything()

if __name__ == "__main__":
    tests()
