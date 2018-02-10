from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #Iterative solution, using STACK to perform InOrder Traversal
    #visit each node in INCREASING order of a BST: depth-first left, root, right...)
    def inOrderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        allNodes = []
        if not root:
            return []
        while (root or stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                allNodes.append(root.val)
                root = root.right
        return allNodes

    def inOrderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.inOrderRecursive(root.left) + [root.val] + self.inOrderRecursive(root.right)
        else:
            return []

    def preOrderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return [root.val] + self.preOrderRecursive(root.left) + self.preOrderRecursive(root.right)
        else:
            return []

    def preOrderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        allNodes = []
        if not root:
            return []
        stack=[root]
        while stack:
            root = stack.pop()
            if root:
                allNodes.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return allNodes

def LevelOrderIterative(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    allNodes = []
    queue = deque()
    if not root:
        return allNodes
    queue.append(root)
    if queue:
        levelNodes = []
        curr = queue.popleft()
        levelNodes.append(curr.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

