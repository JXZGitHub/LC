# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode

        Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
        Calling next() will return the next smallest number in the BST.
        Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

        The constructor uses a stack to implement the 'push all left nodes of a root' into a stack' part of dfs (in order traversal)
        Then the next() method pops one off the stack, uses that as return value, and push all the left children of that node's right child (if any).
        """
        self.stack = deque()
        # This is the 'push all left children onto stack' part of a traditional DFS.
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        #THis is the 'pop off the stack' part of a traditional DFS.
        if self.stack:
            root = self.stack.pop()
            if root.right:
                res = root.right
                while res:
                    self.stack.append(res)
                    res=res.left
            return root.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())