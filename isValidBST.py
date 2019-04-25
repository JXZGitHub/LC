class Solution:
    def isValidBST(self, root):
        """
        Time: O(N)
        Space: O(log(N))
        Keep inorder traversing the tree until an invalid condition occurs.
        """
        stack = []
        prev = float('-inf')
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if prev>=node.val:
                    return False
                else:
                    prev = node.val
                root = node.right
        return True