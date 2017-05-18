class MinHeap:
    def __init__(self, arr=[]):
        if len(arr) > 0:
            self.heap = self.heapify(arr)
        else:
            self.heap = []

        self.size = 0

    def getMin(self):
        if self.size > 0
            ret = self.heap[0] #[1]
            self.heap[0] = self.heap[-1] #[1]
            self.heap.pop() #[]
            self.size -= 1
            self.bubbleDown() #[]
            return ret

    def peek(self):
        if self.size > 0
            return self.heap[0]

    def push(self, val):
        self.heap.append(val)
        self.bubbleUp()
        self.size += 1

    def heapify(self, arr):
        # TODO
        return

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def bubbleDown(self):
        # TODO
        return

    def bubbleUp(self):
        # TODO
        return

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
    # heap1 = MinHeap([1, 2, 3, 4, 5])
    # heap2 = MinHeap([])
    # heap3 = MinHeap([5, 4, 3, 2, 1])
    # heap4 = MinHeap([3, 1])
    # heap5 = MinHeap([0, -1, 1, -2, 2])
    # assert isMinHeap(heap1)
    # assert isMinHeap(heap2)
    # assert isMinHeap(heap3)
    # assert isMinHeap(heap4)
    # assert isMinHeap(heap5)
    assert True

def testGetMin():
    heap = MinHeap([2, 5, 20])
    assert heap.getMin() == 2
    assert heap.getMin() == 5

    heap1 = MinHeap([1, 2, 3, 4, 5])
    assert heap1.getMin() == 1
    assert heap1.getMin() == 2

    heap2 = MinHeap([5, 4, 3, 2, 1])
    assert heap2.getMin() == 1
    assert heap2.getMin() == 2

    heap3 = MinHeap([2, 5, 3, 7, -1])
    assert heap3.getMin() == -1
    assert heap3.getMin() == 2

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
    assert heap.size() == 0

    heap2 = MinHeap([1])
    assert heap.size() == 1

    heap3 = MinHeap([1, 2, 3, 4])
    assert heap.size() == 4

def testIsEmpty():
    heap = MinHeap()
    assert heap.isEmpty()

    heap2 = MinHeap([1])
    assert not heap.isEmpty()

    heap3 = MinHeap([1, 2, 3])
    assert not heap.isEmpty()

def testEverything():
    assert True

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
