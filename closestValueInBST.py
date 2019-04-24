# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int

        Does a DFS with in order traversal, and as soon as target's value is between 2 nodes, find the closer one and return target.
        If target bigger than all nodes, return the last popped node in stack (largest in value)
        If target is smaller than all nodes, then it'll get caught when first node is popped due to prev initialized to -inf.

        Time: O(N)
        Space: O(N) on heap, O(log(N)) on call stack.
        """
        stack = []
        prev = float('-inf')
        ret = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if prev <= target <= node.val:
                    if abs(target - prev) < abs(target - node.val):
                        return prev
                    else:
                        return node.val
                if node.right:
                    stack.append(node.right)
                root = node.right
                prev = node.val
        return node.val

    def closestValue2(self, root, target):
        ret = root.val
        while root:
            if abs(root.val - target) < abs(ret - target):
                ret = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return ret
