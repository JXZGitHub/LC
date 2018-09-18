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


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        BFS
        Time: O(N)
        Space: O(N)
        """
        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)

        return res