from collections import deque

class MaxHeap:
    def __init__(self, arr=[]):
        self.data = deque()
        self.size = 0
        if len(arr) > 0:
            self.size = len(arr)
            self.__heapify(arr)

    def getMax(self):
        if self.size > 0:
            ret = self.data.popleft()
            self.size -= 1
            self.data.appendleft(self.data.pop())
            self.__bubbleDown(0)
            return ret

    def peek(self):
        if self.size > 0:
            return self.data[0]

    def push(self, val):
        self.data.append(val)
        self.size += 1
        self.__bubbleUp(self.size-1)

    def isEmpty(self):
        return self.size == 0

    def __heapify(self, arr):
        self.data = deque(arr)
        for i in xrange(len(arr)-1, -1, -1):
            self.__bubbleDown(i)

    def __bubbleDown(self, index):
        left = self.__left(index)
        right = self.__right(index)

        larger = index

        if left < self.size and self.data[index] < self.data[left]:
            larger = left

        if right < self.size and self.data[left] < self.data[right]:
            larger = right

        if larger != index:
            self.data[larger], self.data[index] = self.data[index], self.data[larger]
            self.__bubbleDown(larger)

    def __bubbleUp(self, index):
        p = self.__parent(index)

        if p >= 0 and self.data[index] > self.data[p]:
            self.data[index], self.data[p] = self.data[p], self.data[index]
            self.__bubbleUp(p)

    def __parent(self, i):
        return i/2

    def __left(self, i):
        return 2*i + 1

    def __right(self, i):
        return 2*i + 2

def testPush():
    h = MaxHeap()
    h.push(2)
    assert h.data[0] == 2

    h.push(3)
    assert h.data[0] == 3

    h.push(1)
    assert h.data[0] == 3

    h.push(5)
    assert h.data[0] == 5

    h.push(-1)
    assert h.data[0] == 5

def testGetMax():
    heap = MaxHeap([2, 5, 20])
    assert heap.getMax() == 20
    assert heap.getMax() == 5

    heap1 = MaxHeap([1, 2, 3, 4, 5])
    assert heap1.getMax() == 5
    assert heap1.getMax() == 4

    heap2 = MaxHeap([5, 4, 3, 2, 1])
    assert heap2.getMax() == 5
    assert heap2.getMax() == 4

    heap3 = MaxHeap([2, 5, 3, 7, -1])
    assert heap3.getMax() == 7
    assert heap3.getMax() == 5

def testPeek():
    heap = MaxHeap([2, 5, 20])
    assert heap.peek() == 20
    assert heap.peek() == 20

    heap1 = MaxHeap([1, 2, 3, 4, 5])
    assert heap1.peek() == 5
    assert heap1.peek() == 5

    heap2 = MaxHeap([5, 4, 3, 2, 1])
    assert heap2.peek() == 5
    assert heap2.peek() == 5

    heap3 = MaxHeap([2, 5, 3, 7, -1])
    assert heap3.peek() == 7
    assert heap3.peek() == 7

def testSize():
    heap = MaxHeap()
    assert heap.size == 0

    heap2 = MaxHeap([1])
    assert heap2.size == 1

    heap3 = MaxHeap([1, 2, 3, 4])
    assert heap3.size == 4

def testIsEmpty():
    heap = MaxHeap()
    assert heap.isEmpty()

    heap2 = MaxHeap([1])
    assert not heap2.isEmpty()

    heap3 = MaxHeap([1, 2, 3])
    assert not heap3.isEmpty()

def testEverything():
    assert True

def tests():
    testPush()
    testGetMax()
    testPeek()
    testSize()
    testIsEmpty()
    testEverything()

if __name__ == "__main__":
    tests()
