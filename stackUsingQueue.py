from LRUCache import LinkedList, ListNode
from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = LinkedList()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        node = ListNode(x, x)
        self.list.insert(node)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        else:
            tail = self.list.tail
            self.list.remove(tail)
            return tail.val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        else:
            return self.list.tail.val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.list.head


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.empty():
            return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.queue)


obj = MyStack2()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.top(), obj.top())
obj.push(4)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.top())
obj.push(99)
print(obj.pop())
print(obj.empty())
