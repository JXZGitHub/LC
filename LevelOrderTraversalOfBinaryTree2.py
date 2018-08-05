from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time: O(N)
        Space: O(N)

        Same as level order traversal, except you reverse the res when returning.
        """
        q = deque()
        res = deque()
        if not root:
            return res
        q.append(root)
        while q:
            size = len(q)
            subRes = []
            for _ in range(size):
                node = q.popleft()
                subRes.append(node.val)
                if node.left:
                    q.append(node.right)
                if node.right:
                    q.append(node.left)
            res.append(subRes)

        return list(reversed(res))
