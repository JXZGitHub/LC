class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """Create
        1) a running previous node that's always one step behind the current nodes being compared.
        2) a fixed node that's one node behind the starting node of the final merged list.
        Time: O(N)
        Space: O(1)
        """
        prev = ListNode(-1)
        preHead = prev
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next #Stay one node behind the most advanced, keeping track of the previous one,

        prev.next = l1 or l2  #One of the list must have reached end (None), so connect prev.next to the start of the surviving list.
        return preHead.next

