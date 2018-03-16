class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return 1+min(self.minDepth(root.right),self.minDepth(root.left))