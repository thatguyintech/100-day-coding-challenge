class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.prevMin = None

class MinStack(object):

    def __init__(self, lst=[]):
        """
        initialize your data structure here.
        """
        self.head = None
        self.minNode = None

        if len(lst) > 0:
            for num in lst:
                self.push(num)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # wrap the value in a node
        newNode = Node(x)

        # empty stack
        if self.head == None:
            self.head = newNode
            self.minNode = newNode

        # existing stack, push the node on top
        else:
            newNode.prev = self.head
            self.head = newNode

            # update the new min
            if x < self.minNode.value:
                newNode.prevMin = self.minNode
                self.minNode = newNode
        return
        

    def pop(self):
        """
        :rtype: void
        """
        # empty stack
        if self.head == None:
            return

        # pop the head
        popped = self.head
        self.head = self.head.prev

        # check if you need to update the min
        if popped.prevMin:
            self.minNode = popped.prevMin

        return popped.value   

    def top(self):
        """
        :rtype: int
        """
        if self.head == None:
            return
        return self.head.value
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minNode == None:
            return
        return self.minNode.value

def tests():
    m = MinStack()
    print(m.pop() == None)
    print(m.push(-1) == None)
    print(m.push(1) == None)
    print(m.push(2) == None)
    print(m.getMin() == -1)
    print(m.top() == 2)
    print(m.pop() == 2)
    print(m.top() == 1)
    print(m.getMin() == -1)

    m = MinStack([-1,1,-2,2,-3,3,0,0,-4,-4])
    print(m.getMin() == -4)
    print(m.pop() == -4)
    print(m.getMin() == -4)
    print(m.pop() == -4)
    print(m.top() == 0)
    print(m.top() == 0)
    print(m.getMin() == -3)

    m = MinStack()
    print(m.top() == None)
    print(m.pop() == None)
    print(m.getMin() == None)
tests()

