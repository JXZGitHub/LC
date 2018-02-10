class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        local_max_sum = float('-inf')
        global_max_sum = local_max_sum
        for x in nums:
            local_max_sum = max(local_max_sum + x, x) #local max is the current max subsum array whose last element is nums[i]
            global_max_sum = max(global_max_sum, local_max_sum)

        return global_max_sum
