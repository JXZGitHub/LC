# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    """
    Idea is to let peak() advance the Iterator to the next item and save that next time.
    And keep a flag to reset 'peeked' to False each time next() is called.
    And the peeked flag can only be reset to False inside next(), this way repeated calls to peek()
    will not keep advancing the pointer, and each call to next() will make next call to peek() pick up a new item again.
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._val = None
        self._hasNext = self.iterator.hasNext()
        self._peeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._peeked:
            self._val = self.iterator.next()
            self._peeked = True
        return self._val  # If it's been peeked before, simply return the 'cached' value

    def next(self):
        """
        :rtype: int
        """
        if not self._peeked:
            self._val = self.iterator.next()

        self._peeked = False  # Once next() is called, then reset this flag so next peek() will advance the pointer again. This is equivalent to 'clearing the cache'
        return self._val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].