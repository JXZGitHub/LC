# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        This solution has an expensive constructor because it processes the entire nestedList to be flat,
        which may not be necessary
        If the user only calls hasNext a few times.
        """
        self.q = deque()
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for l in nestedList:
            if l.isInteger():
                self.q.append(l.getInteger())
            else:
                self.flatten(l.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator2(object):
    """This solution pops all elements of nestedList onto stack during constructor, but does not flatten them.
        It flattens up to the next integer during hasNext, and leaves the remaining of the stack intact until next time."""

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.flatten(self.stack, nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop().getInteger()
        else:
            return False

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if self.stack[-1].isInteger():
                return True  # As soon as we get an integer, we stop flattenning further (until next hasNext())
            subList = self.stack.pop().getList()
            self.flatten(self.stack, subList)
        return False

    def flatten(self, stack, nestedList):
        for i in range(len(nestedList) - 1, -1, -1):
            stack.append(nestedList[i])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())