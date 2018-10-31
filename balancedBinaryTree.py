import math
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        DFS:

        Time: O(N)
        Space: O(Log(N)) on stack. O(1) on heap.
        """
        return self.recurse(root)[-1]

    def recurse(self, root):
        if not root:
            return 0, True
        leftDepth, leftIsBalanced = self.recurse(root.left)
        rightDepth, rightIsBalanced = self.recurse(root.right)
        leftDepth += 1
        rightDepth += 1
        if leftIsBalanced and leftIsBalanced and math.fabs(leftDepth - rightDepth) <= 1:
            return max(leftDepth, rightDepth), True
        else:
            return 0, False #As soon as a subtree node is found to be unbalanced, this will continue flowing up the stack, skipping any checking of depth.