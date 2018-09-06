# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: Stack frame: O(log(N) on balanced tree, O(N) on skewed tree). Heap: O(1)
        """
        return self.recurse(root, 0)[2]

    def recurse(self, root, maxLen):
        if not root:
            return 0, 0, maxLen

        leftInc, leftDec, maxLen = self.recurse(root.left, maxLen)
        rightInc, rightDec, maxLen = self.recurse(root.right, maxLen)

        # This is the current number of nodes of increasing and decreasing sequence ending at the current node.
        # It can be 'reset' to 1, at any given function call during recursion as soon as the current node is not
        # consecutive with its children in either direction.
        inc, dec = 1, 1
        if root.left:
            if root.val - root.left.val == 1:
                inc = max(inc, 1 + leftInc) # +1 is to include the current node in the sequence length
            elif root.val - root.left.val == -1:
                dec = max(dec, 1 + leftDec)

        if root.right:
            if root.val - root.right.val == 1:
                inc = max(inc, 1 + rightInc)
            elif root.val - root.right.val == -1:
                dec = max(dec, 1 + rightDec)

        maxLen = max(inc + dec - 1, maxLen)
        return inc, dec, maxLen