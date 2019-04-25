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


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode

        Time O(N)
        Space O(log(N))

        Just in order traversal while looking for the target.
        """
        stack = []
        found = False
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if found:
                    return node
                root = node.right
                if node == p:
                    found = True
        return None