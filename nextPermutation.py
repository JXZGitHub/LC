class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Time: O(N)
        Space: O(1)
        """
        # Start searching from the end, and stop at the first element that is less than its next element: (1,2,3,7,6,5), index at 3 will be stopped at.
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # If the stopped element is still in the array (ie, array is not completely descending), then start searching from end again, but this time find the first element that is greater than the stopped element: eg (1,2,3,7,6,5), 5 will be the first element from the end that is greater than 3.
        if i >= 0:
            k = len(nums) - 1
            while k >= 0 and nums[k] <= nums[i]:
                k -= 1
            # Swap the stopped element and the first element greater than that from the end: (1,2,3,7,6,5) -> (1,2,5,7,6,3)
            nums[i], nums[k] = nums[k], nums[i]

        # Finally, reverse the subarray after the stopped elememnt's position, to get the next largest permuation (1,2,5,7,6,3) -> (1,2,5,3,6,7), do this for a completely descending array too (which will return the smallest permutation)
        self.reverse(i + 1, len(nums) - 1, nums)

    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1