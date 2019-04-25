# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time O(N)
        Space: O(log(N))
        """
        return self.isMirror(root.left, root.right)
    def isMirror(self, t1, t2):
        if not t1 or not t2:
            return False
        if not t1 and not t2:
            return True
        return t1.val == t2.val and \
               self.isMirror(t1.left, t2.right) and \
               self.isMirror(t1.right, t2.left)

    def isSymmetric2(self, root):
        """
        BFS: maintain 2 queues. Each queue contains the left and right subtree nodes of root except, accept push left and right on one queue, and right and left on the other queue. Compare the node pairs as fetched from queue, only continue if their values are equal.

        Time: O(N)
        Space:O(N)
        """
        if not root:
            return True
        q1, q2 = [root.left], [root.right]
        while q1 and q2:
            new_q1, new_q2 = [], []
            for n1, n2 in zip(q1, q2):
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                new_q1.append(n1.left)
                new_q1.append(n1.right)
                new_q2.append(n2.right)
                new_q2.append(n2.left)
            q1, q2 = new_q1, new_q2
        return True

