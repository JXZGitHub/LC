# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def addToList(self, x):
        currNode = self
        while (currNode.next):
            currNode = currNode.next
        currNode.next = type(self)(x)

    def printList(self):
        currNode = self
        while (currNode):
            print (currNode.val)
            currNode = currNode.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self.listToValue(l1) + self.listToValue(l2)
        digits = self.splitNumberToDigits(sum)
        sumList = self.digitsToList(digits)
        sumList.printList()

    def listToValue(self, l1):
        multiplier = 1
        sum = 0
        while (l1):
            sum = sum + l1.val * multiplier
            multiplier = multiplier * 10
            l1 = l1.next
        return sum

    def splitNumberToDigits(self, sum):
        num = sum
        digits = []
        if num == 0:
            digits.append(num)
        while (num > 0):
            digit = num % 10
            digits.append(digit)
            num = int(num/10)
        #digits.reverse()
        return digits

    def digitsToList(self, digits):
        if digits:
            sumList = ListNode(x=digits[0])
            for d in digits[1:]:
                sumList.addToList(d)
        return sumList

if __name__ == '__main__':
    sol = Solution()
    l1=ListNode(x=2)
    l1.next = ListNode(x=4)
    l1.next.next = ListNode(x=3)
    l2 = ListNode(x=5)
    l2.next = ListNode(x=6)
    l2.next.next = ListNode(x=4)
    sol.addTwoNumbers(l1,l2)




