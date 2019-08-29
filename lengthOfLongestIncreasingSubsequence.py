class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr_len = max_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                max_len = max(curr_len,max_len)
            else:
                curr_len = 1
        return max_len