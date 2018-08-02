# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Time: O(N)
        Space: O(N)

        BFS on the tree using a queue, decrement 'level' by 1 on a node's left node, and increment level by 1 on its right node.
        And use a dictionary to keep track of level:list[TreeNode] as each node is popped off of the queue.
        Print out all values for each key of the dict, where the key must be iterated from least (left most) to biggest (right most).
        """
        level = 0
        q = deque()
        res = []
        if root:
            q.append((root, level))
        else:
            return res
        levelToVal = defaultdict(list)
        leftMost, rightMost = 0, 0
        while q:
            (node, level) = q.popleft()
            levelToVal[level].append(node.val)
            leftMost = min(leftMost, level)
            rightMost = max(rightMost, level)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        for i in range(leftMost, rightMost + 1):
            res.append(levelToVal[i])

        return res

