# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

        Output: 4

        Time: O(N)
        Space: O(log(n) in balanced tree, n in skewed tree)

        """
        _, res = self.recurse(root, 0)
        return res

    def recurse(self, root, res):
        if not root:
            return (True, res)
        # Returning 2 outputs: true/false alongside res (updated count of univalue trees), it avoids using self.res
        # as a class-level varibale.
        left, res = self.recurse(root.left, res)
        right, res = self.recurse(root.right, res)
        if left and right:  # If the current node is still being considered (both subtrees are still 'alive')
            if (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                res += 1
                return (True, res)
        return (False, res)  # Otherwise, no need to consider current node in the parent recursion, as this node cannot have any univalue tree anymore.

