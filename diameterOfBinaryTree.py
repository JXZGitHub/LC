# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space: O(log(N), aka height of tree) on stack frame.

        At each node, its diameter is max depth (# of nodes)
        of its right subtree + max depth of its left subtree.

        So we compute that max depth of each node's right and left subtree and keep track of the largest of this value.

        To do the above, we simpy perform a recursive find max depth starting with root, and during each recursive call,
        we update a global 'maxDiameter' to be the sum of a node's left and right subtree.
        """
        self.maxDepthOfTree(root)
        return self.maxDiameter

    def maxDepthOfTree(self, root):
        if not root:
            return 0
        leftMaxDepth = self.maxDepthOfTree(root.left)
        rightMaxDepth = self.maxDepthOfTree(root.right)
        self.maxDiameter = max(self.maxDiameter, leftMaxDepth + rightMaxDepth)  # Keep track of the highest of (left tree's max depth + right tree's max depth)
        return max(leftMaxDepth, rightMaxDepth) + 1  # Max depth (number of nodes) of a given node


class Solution_without_class_level_variable(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root, 0)[1]

    def depth(self, root, diameter):
        if not root:
            return 0, diameter
        left, diameter = self.depth(root.left, diameter)
        right, diameter = self.depth(root.right, diameter)
        # 'diameter' will be persistent, and if surpassed, will be updated.
        return 1 + max(left, right), max(diameter, left + right)  # Returns max depth of tree and max diameter so far


