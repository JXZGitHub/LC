# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        Do a DFS (using stack) with in-order. And increment count each time a node is popped off the stack, return
        the node when count reaches k
        """
        count = 0
        stack = []
        while (root or stack):
            if root:
                stack.append(root)
                root=root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right