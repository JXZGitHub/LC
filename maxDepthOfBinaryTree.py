# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Recursive:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: O(log(N)) on stack frame. O(1) on heap.
        """
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


class Solution_Inorder_Iterative:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Inorder Iterative

        Time: O(N)
        Space: O(Log(N)) on heap.

        """
        stack = []
        depth = 0
        maxDepth = 0
        while root or stack:
            if root:
                depth += 1
                maxDepth = max(depth, maxDepth)
                stack.append((root, depth))
                root = root.left
            else:
                node, depth = stack.pop()
                root = node.right
        return maxDepth


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Preorder iterative

        Time: O(N)
        Space: O(Log(N)) on heap.
        """
        if not root:
            return 0
        depth = 1
        stack = [(root, depth)]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return maxDepth