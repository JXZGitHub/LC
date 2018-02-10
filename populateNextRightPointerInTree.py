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
    # A BFS using queue, but use a for loop to loop through the size of the queue at every 'level' of the tree,
    # and re-assign the 'next' pointers for each member of the queue at each level.
    def connect(self, root):
        q = deque()
        if root:
            q.append(root)
        while q:
            prev_node=None
            q_size = len(q)
            for i in range(q_size):
                #Instead of popping the queue one at a time at each while's itgeration, pop it ALL during the for loop.
                #At each level of the tree, the members of the queues are always left to right nodes on that level.
                node = q.popleft()
                if prev_node:
                    prev_node.next = node
                prev_node = node #Remember the previous node on the same level
                if prev_node.left:
                    q.append(prev_node.left)
                if prev_node.right:
                    q.append(prev_node.right)