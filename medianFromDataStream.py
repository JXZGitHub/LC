from heapq import *


class MedianFinder:
    """
    The invariant of the algorithm is two heaps, small and large, each represent half of the current list.
    The length of smaller half is kept to be n / 2 at all time and the length of the larger half is
    either n / 2 or n / 2 + 1 depend on n’s parity.
    This way we only need to peek the two heaps’ top number to calculate median.
    """
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # -heappushpop here keeps all values' signs flipped on the small heap to implement a max-heap
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# print (obj.findMedian())
obj.addNum(2)
# print (obj.findMedian())
obj.addNum(1)
# print (obj.findMedian())
obj.addNum(5)
# print (obj.findMedian())
obj.addNum(3)
# print (obj.findMedian())
obj.addNum(4)
# print (obj.findMedian())
print (obj.small, obj.large)