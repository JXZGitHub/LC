# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    #Iterative solution, using STACK to perform InOrder Traversal
    #(visit each node in INCREASING order of a BST: depth-first left, root, right...)
    #At each visitation, check if current one is bigger than previous, as long as it is, continue, otherwise return False.
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        previous = float('-inf')
        if not root:
            return True
        while (root or stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if previous >= root.val:
                    return False
                previous = root.val
                root = root.right
        return True

class Solution2:
    #Recursive method.
    def isValidBST(self, root, ceiling=float('inf'), floor=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val < ceiling and root.val > floor:
            return self.isValidBST(root.left,  root.val, floor) and \
                   self.isValidBST(root.right, ceiling, root.val)
        else:
            return False
