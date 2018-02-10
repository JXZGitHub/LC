from collections import deque
class Solution(object):
    def invertTree(self, root): #Recursive.
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        temp = root.left #Must use a temporary node to save left, as otherwise it'll get changed in the recursive call.
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

class Solution(object):
    def invertTree(self, root): #Iterative, same as BFS using queue,
        # except exchange a node's left and right children as each node is popped off the queue
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = deque()
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root