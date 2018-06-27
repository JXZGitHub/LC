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
        # When a new item arrives, if small heap is same size as large heap, put the new item in small heap and squeeze largest from small heap to big heap.
        # If large heap is longer than small heap, put item in large heap, and squeeze the smallest from large heap into small heap.
        if len(self.small) == len(self.large):
            #If small and large is same size:
            # 1) push the new element into small (but negated version, as all elements in the small heap are kept as
            # negative to  achieve a max heap),
            # 2) pop the smallest from the small heap (in reality maximum absolute value)
            # 3) Then put that value (negated again) from small heap onto big heap.
            heappush(self.large, -heappushpop(self.small, -num))
            # The -num is used to ensure small heap is a max heap.
            # The -heappushpop is to negate whatever is popped off the small heap before inserting into large heap
            # as that's the real value.

        else:
            # -heappushpop here keeps all values' signs flipped on the small heap to achieve a max-heap.
            heappush(self.small, -heappushpop(self.large, num)) #Now both heaps are equal in number again.

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0 #It's subracting self.small[0] because everything in small heap is negative.
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