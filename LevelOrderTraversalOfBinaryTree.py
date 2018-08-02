from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time: O(N)
        Space: O(N)
        """
        res, subRes = [], []
        queue = deque()
        if not root:
            return res
        queue.append(root)
        while queue:
            nodeCountInLevel = len(queue)  # The number of nodes in the next level of the tree
            subRes = []
            for _ in range(nodeCountInLevel):
                node = queue.popleft()
                subRes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subRes)
        return res

    def levelOrder_recursive(self, root):
        res = []
        self.recurse(root, 0, res)
        return res

    def recurse(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.recurse(node.left, level + 1, res)
        if node.right:
            self.recurse(node.right, level + 1, res)

    def levelOrder_iterative_no_for_loop(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time: O(N)
        Space: O(N)

        """
        res, subRes = [], []
        queue = deque()
        if not root:
            return res
        level, prevLevel = 0, 0
        queue.append((root, level))
        while queue:
            node, level = queue.popleft()
            if level > prevLevel:
                res.append(subRes)
                subRes = []
            subRes.append(node.val)
            prevLevel = level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        if subRes:
            res.append(subRes)
        return res