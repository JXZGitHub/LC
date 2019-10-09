class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        Sort intervals by starting location smallest first.
        Then iterate through each interval: keeping track of the current boundaries
        (curr_s and curr_e) of the 'current' interval (before adding to result).

        The condition for adding is if the latest starting location is > current boundary's
        ending location.

        If so, add the current boundaries, and update current boundaries to the latest interval and continue.
        Otherwise, just keep expanding the right boundary of the current interval.
        """
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals)
        curr_s, curr_e = intervals[0]
        for s, e in intervals:
            if s > curr_e:
                res.append([curr_s, curr_e])
                curr_s = s
                curr_e = e
            else:
                curr_e = max(curr_e, e)
        res.append([curr_s, curr_e])
        return res

sol = Solution()
print (sol.merge([[1,5],[2,6]]))
