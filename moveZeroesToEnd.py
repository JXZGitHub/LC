class Solution:
    """
    Time: O(N)
    Space: O(1)
    """
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mostRecentNonZeroIndex = 0

        # Shuffle all the non zeroes to the front of the list, incrementing mostRecentNonZeroIndex each time a non zero occupies a front position.
        for n in nums:
            if n != 0:
                nums[mostRecentNonZeroIndex] = n
                mostRecentNonZeroIndex += 1

                # Starting with mostRecentNonZeroIndex, the rest of the list must be the original zeroes that were replaced.
        for i in range(mostRecentNonZeroIndex, len(nums)):
            nums[i] = 0

    def moveZeroes_many_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Swap each non zero with mostRecentNonZeroIndex, and  then increment mostRecentNonZeroIndex by 1.
        """
        mostRecentNonZeroIndex = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[i], nums[mostRecentNonZeroIndex] = nums[mostRecentNonZeroIndex], nums[i]
                mostRecentNonZeroIndex += 1

