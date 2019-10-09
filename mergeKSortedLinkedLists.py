import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head=currNode=ListNode(-1)
        heap = []
        for l in lists:
            if l:
                #Pushes all first nodes of all lists into a heap.
                heapq.heappush(heap,(l.val, l))
        while heap:
            #Then keep popping off the heap, and whatever is popped off is the next the currNode, and advance the currNode to what's just popped off
            #and push into the heap the next one of the list node that's popped off.
            poppedVal, poppedNode = heapq.heappop(heap)
            if poppedNode.next:
                heapq.heappush(heap, (poppedNode.next.val, poppedNode.next))
            currNode.next = poppedNode
            currNode = currNode.next

        return head.next