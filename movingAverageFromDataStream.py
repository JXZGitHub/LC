from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.size:
            leastRecentVal = self.q.popleft()
            self.sum -= leastRecentVal
        self.q.append(val)
        self.sum += val
        return self.sum / len(self.q)

m = MovingAverage(3)
print (m.next(1), m.next(10), m.next(3), m.next(5))
