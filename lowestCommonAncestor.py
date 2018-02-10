# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == q or root == p:
            return root #A node can be its own root.

        lcaFromLeftSubTree = self.lowestCommonAncestor(root.left, p, q)
        lcaFromRightSubTree = self.lowestCommonAncestor(root.right, p, q)
        if lcaFromLeftSubTree and lcaFromRightSubTree:
            return root #If p and q exist in the 2 subtres separately, then their lca must be the root.
        elif lcaFromLeftSubTree:
            return lcaFromLeftSubTree
        else:
            return lcaFromRightSubTree


class Solution2(object):
    '''
    Iterative: use a BFS (queue) to traverse all nodes from root and build a {node:parent} dict. Then add each
    ancestor of p (including p itself) into a set, and see if q's ancestors are in the set. As soon as one of q's ancestors
    is in the set, return q.
    '''
    def lowestCommonAncestor(self, root, p, q):
        queue = deque()
        if not root:
            return None
        if root == p or root == q:
            return root
        parents = {root: None}
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q