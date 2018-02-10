class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        #If p (given node from which to find successor) has right tree, then find minimum (left most) of the right subtree
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        #if p only has left subtree, find its direct parent starting from root of tree.
        successor = None
        while root and root != p:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor