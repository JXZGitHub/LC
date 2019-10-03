"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        newNode = Node(insertVal, None)
        if not head:
            return newNode
        itr = head
        inserted = False
        while True:
            # Insert between itr and itr.next when insertValue is between itr and itr.next or
            # when insertValue is > than the maximum value (itr is last node before repeating)
            # when insertValue is < than the minimum value (itr is last node before repeating)
            if (itr.val <= insertVal <= itr.next.val) or \
                    (itr.val > itr.next.val and insertVal > itr.val) or \
                    (itr.val > itr.next.val and insertVal < itr.next.val):
                newNode.next = itr.next
                itr.next = newNode
                inserted = True
                break
            itr = itr.next

            if itr == head:
                break  # when cycle seen, then dont continue

        if not inserted:  # All values are same on all nodes, so insert anywhere
            newNode.next = itr.next
            itr.next = newNode
        return head


