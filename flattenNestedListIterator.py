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


class NestedIterator2(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        This solution pops all elements of nestedList onto stack during constructor, but does not flatten them.
        It flattens only what's necessary during hasNext, and leaves the remaining of the stack intact until next time.
        """
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):  # Put all elements onto stack, but starting at end of nestedList
            self.stack.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while (self.stack):
            if self.stack[-1].isInteger():
                return True
            #Start to flatten the poppped element of the stack if it's not integer
            subList = self.stack.pop().getList()
            for i in range(len(subList) - 1, -1, -1):
                self.stack.append(subList[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())