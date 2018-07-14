class Vector2D(object):
    """
    This solution has O(1) in constructor, simply keeps track of current row and col.
    """

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row, self.col = 0, 0
        self.v = vec2d

    def next(self):
        """
        :rtype: int
        """
        result = self.v[self.row][self.col]
        self.col += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.v):
            while self.col < len(self.v[self.row]):  # This will skip empty lists.
                # Col was incremented by 1 in the .next() call prior, so it may already be out of bounds for a given row
                return True
            # If col was out of bound, move to next row and reset col
            self.col = 0
            self.row += 1
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


class Vector2D_2(object):
    """
    Same idea as Flatten Nested List Iterator.

    But this solution is expensive in this problem: constructor is O(N)
    as there's no need to process the entire vec2d during initialization.
    """

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.stack = []
        for i in range(len(vec2d) - 1, -1, -1):  # Pop off each item of the 2d vector in reverse order and put on stack
            self.stack.append(vec2d[i])

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:  # Flatten any lists off the stack and put back the individual integers back onto top of stack.
            listOrNum = self.stack[-1]
            if isinstance(listOrNum, int):
                return True
            self.stack.pop()
            for i in range(len(listOrNum) - 1, -1, -1):
                self.stack.append(listOrNum[i])
        return False


# Your Vector2D object will be instantiated and called as such:
i, v = Vector2D([[1],[],[2,3,4],[]]), []
while i.hasNext():
    v.append(i.next())
print (v)

i, v = Vector2D_2([[1],[],[2,3,4],[]]), []
while i.hasNext():
    v.append(i.next())
print (v)
