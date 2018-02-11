# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        #Sort all intervals by start, then if an interval's start is more than the previous interval's end,
        #a new final interval exists, else, you can adjust the previous interval's end, no need to care about start.
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        finalIntervals = []
        for interval in intervals:
            if not finalIntervals or finalIntervals[-1].end < interval.start:
                finalIntervals.append(interval)
            else:
                finalIntervals[-1].end = max(finalIntervals[-1].end,interval.end)

        return finalIntervals

sol = Solution()
Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)
print (sol.merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]))
