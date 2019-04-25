# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool

        Time: O(len(s) * len(t))
        Space: O(log(len(s))
        """
        if not s:
            return False
        if self.isEqual(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isEqual(self, a, b):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        else:
            return a.val == b.val and self.isEqual(a.left, b.left) and self.isEqual(a.right, b.right)