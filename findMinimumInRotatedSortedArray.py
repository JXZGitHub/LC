class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time: O(log N)
        Space: O(1)

        After rotation, array consists of the first increasing segment, and 2nd increasing segment.
        First segment has every element bigger than those in the 2nd increasing segment.

        Binary Search: first check if the array is rotated (first is < last means it's NOT rotated anymore),
        if not, then just reurn first element.

        If it's rotated, determine if the minimum is in the 1st increasing segment or 2nd increasing segment.

        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] < nums[end]:
                return nums[start]  # array is no longer rotated, just return first as min.

            mid = start + (end - start) // 2
            n = nums[mid]
            if n >= nums[start]:
                start = mid + 1  # We are still in the first increasing segment, so search in 2nd half.
            elif n < nums[start]:
                end = mid  # We are in the 2nd increasing segment (every element of it is smaller than first), search in 2nd half but INCLUDING the current mid point as that might just be the minimum itself.

        return nums[start - 1]  # if this loop exits, start would be 1 over the boundary of the array.