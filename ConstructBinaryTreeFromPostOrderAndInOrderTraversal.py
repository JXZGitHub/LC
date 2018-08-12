# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode

        Time: O(N log (N) for balanced tree, N^2 for skewed tree)
        Space: O(N)

        Same algorithm as construct binary tree from preorder and inorder traversal, except postorder means
        the last element of a initial post order list is the root, and the next root location in postorder list
        is either last-1, or last-(size of right subtree)
        """
        return self.recurse(0, len(inorder) - 1, len(postorder) - 1, inorder, postorder)

    def recurse(self, inStart, inEnd, postStart, inorder, postorder):
        if inEnd < inStart:
            return None
        parent = postorder[postStart]
        node = TreeNode(parent)
        for i in range(inStart, inEnd + 1):
            if inorder[i] == parent:
                node.right = self.recurse(i + 1, inEnd, postStart - 1, inorder, postorder)
                node.left = self.recurse(inStart, i - 1, postStart - (inEnd - i + 1), inorder, postorder)
                #(inEnd-i+1) is the number of nodes in the right subtree, which we have to skip over to find the next root.
                break
        return node

