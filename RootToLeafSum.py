# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root:
            stack = [(root,root.val)]
        else:
            return 0
        while stack:
            root, val = stack.pop()
            if not root.right and not root.left:
                sum += val #when its a leaf, then we can add all the accumulated val's from before.
            if root.right:
                stack.append((root.right,root.right.val+val*10)) #for every deeper level, multiple previous one by 10 and ad().
            if root.left:
                stack.append((root.left,root.left.val+val*10))
        return sum

class Solution2:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time: O(N)
        Space O(Log(N))
        """

        return self.recurse(root, 0)

    def recurse(self, root, prevNumber):
        if not root:
            return 0
        currNumber = prevNumber * 10 + root.val
        if not root.left and not root.right:
            return currNumber
        else:
            return self.recurse(root.left, currNumber) + self.recurse(root.right, currNumber)
