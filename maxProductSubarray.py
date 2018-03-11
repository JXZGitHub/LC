class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Find the contiguous subarray within an array (containing at least one number) which has the largest product.

        For example, given the array [2,3,-2,4],
        the contiguous subarray [2,3] has the largest product = 6.

        Keep tracking of curr_max and curr_min as max and min products of nums[i]
        """
        global_max=curr_max=curr_min=nums[0]

        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                #if current number is negative, then previous max becomes min, and min becomes max. So swap them.
                #Because the when muitplied by this number, previous max will end up with a min, and vice versa.
                curr_max,curr_min=curr_min,curr_max

            #update curr_max and curr_min just like max sum subarray problem.
            curr_max=max(curr_max*n, n)
            curr_min=min(curr_min*n, n)

            #update global MAX just like max sum subarray problem.
            global_max=max(global_max,curr_max)

        return global_max