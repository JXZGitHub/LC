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
        if not nums:
            return [-1, -1]
        res = []
        index = -1
        # LEFT BOUNDARY: find the position of the last element that's <= target
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            if nums[mid] == target:
                index = mid
        res.append(index)

        # RIGHT BOUNDARY: find the position of first element thats that's >= target
        index = -1
        start, end = end, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if target >= nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            if nums[mid] == target:
                index = mid
        res.append(index)
        return res