# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]

        Time: O(N*log(N)), we visit each node once, but we do a string concatenation each time (because string is not mutable)
                        , which can have as many chars as height of tree)
        Space: O(log(N)), which is height of tree)
        """
        res = []
        if not root:
            return res
        self.recurse(root, '', res)
        return res

    def recurse(self, node, previousPath, res):
        if not node.left and not node.right:
            res.append(previousPath + str(node.val))
            return
        if node.left:
            self.recurse(node.left, previousPath + str(node.val) + '->',
                         res)  # String is immkutable ,so previousPath+str(node.val) is O(H) operation, where H is height of tree. (ie, the length of previousPath can be as many chars as height of the tree)
        if node.right:
            self.recurse(node.right, previousPath + str(node.val) + '->', res)

