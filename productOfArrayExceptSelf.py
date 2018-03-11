class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        First, scan left to right, fill in res[i] as product of all nums before position i.
        Then, scan right to left, and update res[i] by multiplying by product of all nums AFTER pos i.
        """
        res = [0 for _ in range(len(nums))]
        res[0] = 1
        right = 1
        # Left to right: fill in res[i] as product of all nums before position i.
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # Now, go right to left, update res[i] by mulitplying by product of all nums AFTER pos i.
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]  # All products including at pos i, to be included in the in the next iteration going left.
        return res