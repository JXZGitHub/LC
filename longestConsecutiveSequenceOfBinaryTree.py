# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution_recursive:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: Stack frame: O(log(N) on balanced tree, N on skewed tree). Heap: O(1)
        """
        return self.recurse(root, 0)[1]

    def recurse(self, root, maxLength):
        if not root:
            return 0, maxLength
        right, maxLength = self.recurse(root.right, maxLength)
        left, maxLength = self.recurse(root.left, maxLength)
        if not root.right or root.val - root.right.val == -1:
            currentRightLength = 1 + right
        else:
            currentRightLength = 1
        if not root.left or root.val - root.left.val == -1:
            currentLeftLength = 1 + left
        else:
            currentLeftLength = 1
        maxLengthAtNode = max(currentLeftLength, currentRightLength)
        maxLength = max(maxLength, maxLengthAtNode)
        return maxLengthAtNode, maxLength

class Solution_more_concise_recursive:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: Stack frame: O(log(N) on balanced tree, N on skewed tree). Heap: O(1)
        """
        if not root:
            return 0
        return self.recurse(root, root.val, 0, 0)

    def recurse(self, root, target, count, maxCount):
        if not root:
            return maxCount
        if root.val == target:
            count += 1
        else:
            count = 1
        maxCount = max(maxCount, count)
        left = self.recurse(root.left, root.val + 1, count, maxCount)
        right = self.recurse(root.right, root.val + 1, count, maxCount)
        return max(left, right)

import collections
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: Heap: O(log(N) on balanced tree, N on skewed tree).
        """
        if not root:
            return 0
        q = collections.deque()
        res = 0
        q.append([root, 1])
        while q:
            node, l = q.pop()
            res = max(res, l)
            if node.left and node.left.val == node.val + 1:
                q.appendleft([node.left, l + 1])
            elif node.left:
                q.appendleft([node.left, 1])
            if node.right and node.right.val == node.val + 1:
                q.appendleft([node.right, l + 1])
            elif node.right:
                q.appendleft([node.right, 1])
        return res

