# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        DFS
        Time: O(N)
        Space: O(Log(N), height of tree)
        """
        res = []
        stack = []
        currLevel = -1
        if not root:
            return res
        while root or stack:
            if root:
                currLevel += 1
                stack.append((root, currLevel))
                if currLevel > len(res) - 1:
                    res.append(root.val)
                else:
                    res[currLevel] = root.val
                root = root.left
            else:
                root, currLevel = stack.pop()
                if currLevel > len(res) - 1:
                    res.append(root.val)
                else:
                    res[currLevel] = root.val
                root = root.right
        return res


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time: O(N)
        Space: (Max of 2 children per node as it's a binary tree)
        """
        q = []
        if root:
            q.append(root)
        res = []
        while q:
            new_q = []
            res.append(q[-1].val)
            for n in q:
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            q = new_q
        return res