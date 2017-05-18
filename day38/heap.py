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
        heap = []
        self.size = len(arr)
        return heap

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

def testPush():
    heap = MinHeap()
    heap.push(2)
    assert heap.root.val == 2

    heap.push(3)
    assert heap.root.val == 2

    heap.push(1)
    assert heap.root.val == 1

    heap.push(5)
    assert heap.root.val == 1

    heap.push(-1)
    assert heap.root.val == -1

def testHeapify():
    def isMinHeap(heap):
        if heap == None:
            return True

        if heap.root.left:
            left = heap.root.val < heap.root.left.val
        else:
            left = True

        if heap.root.right:
            right = heap.root.val < heap.root.right.val
        else:
            right = True

        return isMinHeap(heap.root.left) and isMinHeap(heap.root.right) and left and right

    heap1 = MinHeap([1, 2, 3, 4, 5])
    heap2 = MinHeap([])
    heap3 = MinHeap([5, 4, 3, 2, 1])
    heap4 = MinHeap([3, 1])
    heap5 = MinHeap([0, -1, 1, -2, 2])
    assert isMinHeap(heap1)
    assert isMinHeap(heap2)
    assert isMinHeap(heap3)
    assert isMinHeap(heap4)
    assert isMinHeap(heap5)

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