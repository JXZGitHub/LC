# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_no_stack:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time: O(N)
        Space: O(max nodes at each level), ~O(N)
        """
        toRight = False
        q = []
        res = []
        if root:
            q.append(root)
        while q:
            output = []
            newQ = []
            for n in q:
                output.append(n.val)
            for i in range(len(q) - 1, -1, -1):
                node = q[i]
                if toRight:
                    order = ['left', 'right']
                else:
                    order = ['right', 'left']
                for o in order:
                    if getattr(node, o):
                        newQ.append(getattr(node, o))
            q = newQ
            toRight = not toRight
            res.append(output)
        return res


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time: O(N)
        Space: O(N)

        For each level, alternatingly insert each node's children into s1 or s2, but in differnet order (left and right on one stack, right and left on another). Then keep popping off each non-emty stack and put into result, and continue until both stacks are empty.
        """
        s1, s2 = [root], []
        res = []
        output = []
        if not root:
            return res
        while s1 or s2:
            # A new level begins, put each node's child in the other stack, in opposite order. So s1 content's children goes into s2.
            while s1:
                node = s1.pop()
                output.append(node.val)
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            if output:
                res.append(output)
                output = []

            # A new level begins, s2's content's children will be in s1...
            while s2:
                node = s2.pop()
                output.append(node.val)
                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
            if output:
                res.append(output)
                output = []
        return res
