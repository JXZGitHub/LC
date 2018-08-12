# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]

        Backtracking + DFS

        Time: O(N)
        Space: O(log(N) on the call frame)
        """
        res = []
        self.recurse(sum, [], root, res)
        return res

    def recurse(self, remainingSum, combo, root, res):
        if not root:
            return
        val = root.val
        combo.append(root.val)
        if root.val == remainingSum and not root.left and not root.right:
            res.append(combo[:])
        self.recurse(remainingSum - root.val, combo, root.left, res)
        self.recurse(remainingSum - root.val, combo, root.right, res)
        combo.pop()  # Only need to pop once because if any of the above recurse calls send in a None
                     # (root.left or root.right is None) into the next call, it'll just return without
                     # adding more to the combo list.


class Solution_Iterative:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]

        Iterative: Inorder traversal using stack.

        Time: O(N)
        Space: O(log(N) on the call frame)
        """
        stack = []
        res = []
        path = []
        val = 0
        visitedNode = None
        while root or stack:
            if root:
                val += root.val
                path.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right and root.right != visitedNode:
                    root = root.right
                    continue
                if not root.left and not root.right and val == sum:
                    res.append(path[:])
                visitedNode = root
                stack.pop()
                val -= root.val
                path.pop()
                root = None
        return res