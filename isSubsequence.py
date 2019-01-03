import collections
import bisect


class Solution:
    def buildCharIndexMap(self, t):
        """
        A map of {each char in t: list of indices it appears in}, in ascending order.
        """
        m = collections.defaultdict(list)
        for i, n in enumerate(t):
            m[n].append(i)
        return m

    def leftBoundary(left, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time O(log N)
        Space: O(1)

        In ascending array, find the position of the last element that's < target OR first element that's = target.
        This is the left boundary
        """
        start, end = 0, len(nums)
        index = None
        while start < end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
        return start


    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = self.buildCharIndexMap(t)
        current_index = 0  # All matches for each char must be >= current_index in t
        for c in s:
            locations = m[c]  # List of locations in t that c exists in.
            found_index = self.leftBoundary(locations,current_index)  # The index to insert 'current_index' into locations to maintain order, snapped to the left.  This is basically the leftest possible location in tthat matches c.
            if found_index == len(locations):
                # The current_index is already bigger than all of locations
                return False
            current_index = locations[found_index] + 1  # The index in t from which to start the next search in.
        return True


class Solution2:
    def isSubsequence_two_pointer(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1
        if p1 == len(s):
            return True
        else:
            return False

sol = Solution()
print (sol.isSubsequence(s='axc',t='ahbgdc'))