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
        """
        if not root:
            return None

        leftNode = self.treeToDoublyList(root.left)
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

