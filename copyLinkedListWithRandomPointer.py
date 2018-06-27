# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """

        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
        Return a deep copy of the list.

        :type head: RandomListNode
        :rtype: RandomListNode
        Time: O(N)
        Space: O(N)

        1) Create a dictionary of <original node: copied node>
        2) Then for every copied node, assign its Next and Random pointers to be WHATEVER COPIED NODE that the original node's.next and .random point to.
        3) Then, all the values of the dictionary is now a complete COPIED linked list.

        """
        if not head:
            return None

        origToCopy = {}

        # 1) Create a dictionary of <original node: copied node>
        node = head
        while node:
            origToCopy[node] = RandomListNode(node.label)
            node = node.next

        # 2) Then for every copied node, assign its Next and Random pointers to be WHATEVER COPIED NODE that the original node's.next and .random point to.
        node = head
        for origNode, copyNode in origToCopy.items():
            copyNode.next = origToCopy.get(origNode.next)
            copyNode.random = origToCopy.get(origNode.random)

        # all the values of the dictionary is now a complete COPIED linked list.
        return origToCopy[head]
