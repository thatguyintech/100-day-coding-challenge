# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, pathSum):
        """
        :type root: TreeNode
        :type pathSum: int
        :rtype: bool
        """
        # empty tree
        if root == None:
            return False

        # leaf node, check sum
        if root.left == None and root.right == None:
            return pathSum == root.val

        # reduce sum and recurse
        reducedSum = pathSum-root.val
        return self.hasPathSum(root.left, reducedSum) or self.hasPathSum(root.right, reducedSum)

def tests():
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)

    s = Solution()
    assert(s.hasPathSum(bt, 1) == False)
    assert(s.hasPathSum(bt, 3) == True)
    assert(s.hasPathSum(bt, 4) == True)

tests()