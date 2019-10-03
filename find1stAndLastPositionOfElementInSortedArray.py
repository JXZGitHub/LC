class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time O(log N)
        Space: O(1)

        This is an equivalent to
        1) In ascending array, find the position of the last element that's <= target. This is the left boundary
        AND
        2) In ascending array, find the position of first element thats that's >= target. This is the right boundary
        And if either boundary is NOT the target itself, assign it as -1.
        """
        lo, hi = 0, len(nums) - 1
        res = [-1, -1]

        # Find left boundary of the first number that is == target
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target <= nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
            if target == nums[mid]:
                res[0] = mid  # Left is updated multiple times as we expand left boundary

        # Find right boundary of the last number that is == target
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
            if target == nums[mid]:
                res[1] = mid  # Left is updated multiple times as we expand left boundary

        return res

sol = Solution()
#print (sol.searchRange([5,7,7,8,8,10],8))
print (sol.searchRange([],8))