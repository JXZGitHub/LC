#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        return self.recurse(0, len(inorder)-1, 0, inorder, preorder)

    def recurse(self, inStart, inEnd, preStart, inorder, preorder):
        if inEnd - inStart < 0:
            return None
        parentValue = preorder[preStart]
        root = TreeNode(parentValue)
        for i in range(inStart,inEnd+1):
            if inorder[i] == parentValue:
                root.left = self.recurse(inStart, i-1,preStart + 1, inorder, preorder)
                root.right = self.recurse(i+1, inEnd, preStart + i - inStart + 1, inorder, preorder)
                #preStart + i - inStart + 1 means
                #to skip over the size of the left subtree to get to the root of the right subtree in the preorder list.
                break
        return root

sol = Solution()
root  = sol.buildTree([3,9,20,15,7],[9,3,15,20,7])
print (root.val, root.left, root.right)