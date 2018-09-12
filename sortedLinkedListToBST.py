#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode

        Time: O(Nlog(N))
        Space: O(log(N)) on stack frame. O(1) on heap.
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        fast = slow = previous = head

        while fast.next and fast.next.next:
            previous = slow
            fast = fast.next.next
            slow = slow.next #Slow will be the midpoint when fast reaches the end.

        fast = slow.next  # fast is the head of the right-side linked-list
        previous.next = None  # previous is he head of the right-side linked-list, BREAK the left-side list.
        parent = TreeNode(slow.val)
        if head != slow:  # If there's more elements to the left of the parent
            parent.left = self.sortedListToBST(head)
        parent.right = self.sortedListToBST(fast)
        return parent

class Solution:
    def sortedListToBST_convert_to_list(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sortedList = []
        while head:
            sortedList.append(head.val)
            head = head.next
        return self.recurse(sortedList, 0, len(sortedList) - 1)

    def recurse(self, sortedList, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(sortedList[start])
        mid = start + ((end - start) // 2)
        parent = TreeNode(sortedList[mid])
        parent.left = self.recurse(sortedList, start, mid - 1)
        parent.right = self.recurse(sortedList, mid + 1, end)
        return parent