# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## My Solution ##
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # stack for storing the children we're overwriting
        store = []

        while root:
            if root.right:
                store.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            elif store:
                root.right = store.pop()

            root = root.right

## Helpers ##

def preorder(node, ret):
    if node:
        ret.append(node.val)
        preorder(node.left, ret)
        preorder(node.right, ret)

# Create a BT like this:
#     1 
#    / \
#   2   5
#  / \ / \
# 3  4 6  7
#
def create_preorder_binary_tree():
    tree_nodes = [TreeNode(i) for i in xrange(1, 8)]
    tree_nodes[0].left = tree_nodes[1]
    tree_nodes[1].left = tree_nodes[2]
    tree_nodes[1].right = tree_nodes[3]
    tree_nodes[0].right = tree_nodes[4]
    tree_nodes[4].left = tree_nodes[5]
    tree_nodes[4].right = tree_nodes[6]

    return tree_nodes[0]

## Tests ##

def test_create_preorder_binary_tree():
    t = create_preorder_binary_tree()

    ret = []
    preorder(t, ret)
    return ret == [1, 2, 3, 4, 5, 6, 7]

def test_regular_solution():
    tree = create_preorder_binary_tree()
    solution = Solution()
    solution.flatten(tree)

    checker = 1
    while tree:
        if tree.val != checker:
            return False
        tree = tree.right
        checker += 1

    return True

# TODO(albert): test more edge cases

def tests():
    print(test_create_preorder_binary_tree())
    print(test_regular_solution())

tests()