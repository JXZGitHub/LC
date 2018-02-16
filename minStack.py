class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    2 Stack solution:
    stack1 keeps track of all pushed/popped elements.
    stack2 keeps track of latest minimums, so only elements smaller or equal to current minimum is pushed to stack2
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if not self.stack2 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack1:
            x = self.stack1.pop()
            if self.stack2 and x == self.stack2[-1]:
                self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack1:
            return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]

class MinStack2:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

    1 Stack solution:
    a single stack, an a min variable to keep tracking of running minimum.

    When pushing a value smaller or equal than existing minimum, push the current minimum (AGAIN) then push the value,
    and update minimum var to the value.

    When popping, if value popped is minimum, update minimum to be the next top value (which must be the previous
    minimum that was pushed ASGAIN before), and pop AGAIN get rid of that redundant previous minimum.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            x = self.stack.pop()
            if x == self.min:
                self.min = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min