# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node

        Do normal in-order iterative traversal (using stack) and link up each node with its previous node as we go.
        Time: O(N)
        Space: O(log(N)) on call stack. O(1) on heap.
        """
        if not root:
            return None
        stack = []
        prev = None
        head = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()

                # Sets the head to be the first element of the linked list (smallest value in BST)
                if not head:
                    head = node

                # Link backwards to its prev node and let prev node link forward
                if prev:
                    node.left = prev  # Backwards to prev
                    prev.right = node  # Forward from prev
                prev = node
                root = node.right

        node.right = head  # Link the last node's forward to the head (first element of list)
        head.left = node  # Link head's backward to the last node
        return head

class Solution2(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        hc = self.treeToDoublyList(root.left)
        rightNode = self.treeToDoublyList(root.right)

        root.left = root
        root.right = root

        return self.joinTwoLists(self.joinTwoLists(leftNode, root), rightNode)

    def joinTwoLists(self, leftList, rightList):
        if not leftList:
            return rightList
        if not rightList:
            return leftList

        leftLast = leftList.left
        rightLast = rightList.left

        leftLast.right = rightList
        rightList.left = leftLast

        leftList.left = rightLast
        rightLast.right = leftList

        return leftList

