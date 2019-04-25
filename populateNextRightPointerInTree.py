from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        if root.right:
            #The 'next' of a root's right child is the left child of the root's own 'next'.
            #If root has no 'next', then its right child has no next either.
            root.right.next = root.next and root.next.left or None
        self.connect(root.right)
        self.connect(root.left)

class Solution:
    # @param root, a tree link node
    # @return nothing
    # A BFS using queue, and at each level connect up each node's next, keeping track of the prev node at each level.
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q = [root]
        while q:
            new_q = []
            prev = None
            for n in q:
                if prev:
                    prev.next = n
                prev = n
                if n and n.left:
                    new_q.append(n.left)
                if n and n.right:
                    new_q.append(n.right)
            q = new_q
        return root