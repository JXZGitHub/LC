class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
        For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
        the contiguous subarray [4,-1,2,1] has the largest sum = 6.

        Time: O(N)
        Space: O(1)

        Dynamic programming.
        DP[i] = maximum sun of a subarray whose last element is nums[i]. So DP[0] = nums[0], and DP[n] = max(dp[n-1]+nums[n], nums[n])
        And we then find the maximum dp[n] of the entire list.

        Except we don't need to store all values of dp in a separate, can we keep updating dp[n] and global max of dp[n] as we go through each number.
        """
        curr_max = nums[0]  # the maximum sum of the subarray that ENDS at current index.
        global_max = curr_max  # the global maximum sum of the subarray in nums

        for i in range(1, len(nums)):
            # for nums[i], the max sum of a subarray that ends at nums[i]  either includes
            # the previous max subarray (previous max subarray + nums[i]), or it does NOT (just nums[i] by itself.)
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(curr_max, global_max)  # curr_max ending at position i may or may not be greater than previously curr_max at previous indices.
        return global_max

sol = Solution()
print (sol.maxSubArray([4,-1,2,1]))