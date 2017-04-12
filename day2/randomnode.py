import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# This approach saves space - O(1) space complexity
# but is slower - O(n) runtime
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.numNodes = 0

        p = self.head
        while p != None:
            self.numNodes += 1
            p = p.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = random.randint(0, self.numNodes-1)
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        return p.val

## Helpers ##

# this is my noob way of checking randomness...
def is_random(f, possibilities):
    d = {i: 0 for i in xrange(1, possibilities+1)}

    for i in xrange(10000):
        d[f()] += 1

    for key in d:
        if not (d[key] > 900 and d[key] < 1100):
            return False

    return True

## Tests ##

# A linked list for testing
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

def test_new_node():
    check = False

    n = Node(2)
    check = (n.val == 2)
    check = (n.next == None)
    return check

def test_linked_list_pointer_connection():
    check = False

    head = Node(1)
    middle = Node(2)
    tail = Node(3)

    head.next = middle
    middle.next = tail

    check = (head.next.next == tail)
    return check

def test_init_solution_sizing():
    check = False

    solution = Solution(n1)
    check = (solution.numNodes == 10)

    return check

def test_get_random_returns_int():
    check = False
    solution = Solution(n1)

    check = (type(solution.getRandom()) == int)

    return check

def test_solution_randomness():
    check = False

    solution = Solution(n1)

    check = (is_random(solution.getRandom, 10))
    return check

def tests():
    print(test_new_node())
    print(test_linked_list_pointer_connection())
    print(test_init_solution_sizing())
    print(test_get_random_returns_int())
    print(test_solution_randomness())

tests()