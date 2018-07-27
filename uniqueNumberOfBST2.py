# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]

        Time: O(Calatan (n), which is O(~4^n / n^(3/2))
        Space:  O(Catalan (n))
        """
        if n == 0:
            return []
        return self.recurse(1, n)

    def recurse(self, start, end):
        res = []
        if start > end:
            res.append(None)  # Base case where there's no number right or left of a root.
            return res
        for i in range(start, end + 1):  # Try each 'i' as the root of the tree
            leftSubTree = self.recurse(start, i - 1)
            rightSubTree = self.recurse(i + 1, end)

            # Make all valid BST', with a given root of i, and a given set of left tree nodes and right tree nodes.
            for leftNode in leftSubTree:
                for rightNode in rightSubTree:
                    root = TreeNode(i)
                    root.right = rightNode
                    root.left = leftNode
                    res.append(root)
        return res
