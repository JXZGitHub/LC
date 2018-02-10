import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head=prev=ListNode(-1)
        heap = []
        for l in lists:
            if l:
                #Pushes all first nodes of all lists into a heap.
                heapq.heappush(heap,(l.val, l))
        while heap:
            #Then keep popping off the heap, and whatever is popped off is the next in the final list,
            #and push into the heap the next one of the list that's popped off.
            currVal, currNode = heapq.heappop(heap)
            prev.next = ListNode(currVal)
            prev = prev.next
            if currNode.next:
                heapq.heappush(heap, (currNode.next.val, currNode.next))

        return head.next

class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head=prev=ListNode(-1)
        heap = []
        for l in lists:
            if l:
                #Pushes all first nodes of all lists into a heap.
                heapq.heappush(heap,(l.val, l))
        while heap:
            #Then keep popping off the heap, and whatever is popped off is the next in the final list,
            #and push into the heap the next one of the list that's popped off.
            currVal, currNode = heapq.heappop(heap)
            prev.next = ListNode(currVal)
            prev = prev.next
            if currNode.next:
                heapq.heappush(heap, (currNode.next.val, currNode.next))

        return head.next