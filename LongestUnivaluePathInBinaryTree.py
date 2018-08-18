# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int


        Given a binary tree, find the length of the longest path where each node in the path has the same value.
        This path may or may not pass through the root.

        Note: The length of path between two nodes is represented by the number of edges between them.

        Example 1:
        Input:

                      5
                     / \
                    4   5
                   / \   \
                  1   1   5
        Output:
        2

        Example 2:
        Input:

                      1
                     / \
                    4   5
                   / \   \
                  4   4   5
        Output:
        2

        Same strategy as finding diameter of binary tree: at any given node, longest univalue path is maximum
        univalue path of its left subtree + maximum univalue path of its right subtree.

        Important to 'reset' (set to 0) at each node's left and right's uni value count, iF the node left or right
        child is not the node's value (the chain is broken), other wise keep adding 1.

        Base case is when it's Null node, then return 0 (length of univalue path of a single side of none is 0)

        Time: O(N)
        Space: O(log(N) for balanced tree, N for skewed tree)
        """
        self.maxUniLen = 0
        self.recurse(root)
        return self.maxUniLen

    def recurse(self, root):
        if not root:
            return 0
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        if root.left and root.left.val == root.val:
            leftUniLen = 1 + left
        else:
            leftUniLen = 0
        if root.right and root.right.val == root.val:
            rightUniLen = 1 + right
        else:
            rightUniLen = 0
        self.maxUniLen = max(self.maxUniLen, leftUniLen + rightUniLen)
        return max(leftUniLen, rightUniLen)
