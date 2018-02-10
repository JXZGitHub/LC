"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node): #RECURSIVE
        # write your code here
        if not root:
            return node
        if node.val > root.val:
            root.right = self.insertNode(root.right, node)
        else:
            root.left = self.insertNode(root.left, node)
        return root

    def insertNode2(self, root, node): #ITERATIVE
        if not root:
            return node
        copyRoot = root
        while root:
            if node.val > root.val:
                if not root.right:
                    root.right = node
                    break
                else:
                    root = root.right
            if node.val < root.val:
                if not root.left:
                    root.left = node
                    break
                else:
                    root = root.left
        return copyRoot