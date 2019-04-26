# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution_BFS(object):
    """
    Time: O(N^2)
    Space: O(N)
    """
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res
        q = [root]
        while q:
            new_q = []
            for n in q:
                d = self.maxD(n.left) + self.maxD(n.right)
                res = max(res, d)
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            q = new_q
        return res

    def maxD(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxD(root.left), self.maxD(root.right))


class Solution_DFS(object):
    """
    Time: O(N)
    Space: O(log(N)) on stack frame. O(1) on heap.

    """
    def diameterOfBinaryTree(self, root):
        return self.recurse(root, 0)[1]

    def recurse(self, root, maxDiameter):
        if not root:
            return 0, maxDiameter

        # This part is just finding max depth
        leftMaxDepth, maxDiameter = self.recurse(root.left, maxDiameter)
        rightMaxDepth, maxDiameter = self.recurse(root.right, maxDiameter)
        maxDepth_from_root = 1 + max(leftMaxDepth, rightMaxDepth)

        # But we also want to keep track of max diameter globally.
        # diameter is sum of left subtree's max depth + right subtree's max depth.
        maxDiameter_global = max(maxDiameter, leftMaxDepth + rightMaxDepth)

        # We return both max_depth from this root, and global max diameter.
        return maxDepth_from_root, maxDiameter_global

class Solution_DFS_using_class_variable(object):
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





