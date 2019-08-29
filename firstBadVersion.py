# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Just binary search

        Time: O(log(n))
        Space: O(1)
        """
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start