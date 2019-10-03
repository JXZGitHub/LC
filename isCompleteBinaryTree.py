import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time O(N)
        Space O(N/2 + 1 -- N): number of leaf nodes of a given tree
        """
        q = collections.deque([root])
        foundNone = False
        while q:
            n = q.pop()
            if n is None:
                foundNone = True
            else:
                if foundNone:
                    return False
                q.appendleft(n.left)
                q.appendleft(n.right)

        return True

root = TreeNode(1)
left = TreeNode(20)
right = TreeNode(20)
root.left=left
root.right=right

sol = Solution()
print (sol.isCompleteTree(root))