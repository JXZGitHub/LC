# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        Time: (n)
        Space: (1)

        Top down: connect the root's left subtree's right most node to the root's right subtree, then keep doing the same to the root's original left subtree (which is now root.right)

        """
        curr = root
        while (curr):
            if curr.left:
                head = curr.left
                while head.right:
                    head = head.right
                head.right = curr.right  # Right most node of the left subtree connects to the right subtree
                curr.right = curr.left
                curr.left = None
            curr = curr.right


class Solution_Recursive:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        Time: (nlog(n))
        Space: (log(n) for balanced tree, n for skewed) on stack frame.
        """
        self.recurse(root)

    def recurse(self, root):
        if not root:
            return None
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        if left:
            self.rightMostNode(left).right = root.right
            root.right = left
            root.left = None
        return root

    def rightMostNode(self, root):
        if not root:
            return None
        if not root.right:
            return root
        return self.rightMostNode(root.right)
