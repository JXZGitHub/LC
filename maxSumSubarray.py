class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
        For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
        the contiguous subarray [4,-1,2,1] has the largest sum = 6.
        """
        global_max = curr_max = nums[0]
        for i in range(1, len(nums)):
            #If the current number is smaller than cumulative sum of all numbers including itself,
            #then keep updating current max., else 'reset' current max to be current number (window restarts at this number)
            curr_max = max(curr_max + nums[i], nums[i])

            #Update global max everytime
            global_max = max(curr_max, global_max)

        return global_max
