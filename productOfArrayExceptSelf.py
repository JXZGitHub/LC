class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        First, scan left to right, fill in res[i] as product of all nums before position i.
        Then, scan right to left, and update res[i] by multiplying by product of all nums AFTER pos i.
        """
        res = [1 for _ in range(len(nums))]
        left = 1
        right = 1

        # Scan left to right, and res[i] is product of everything BEFORE nums[i]
        for i in range(len(res)):
            res[i] = left * res[i]
            left = left * nums[i]  # Keeps tracking of product of everything so far from left.

        # Then scan right to left, and res[i] = res[i] * product of everything AFTER nums[i]
        for i in range(len(res) - 1, -1, -1):
            res[i] = right * res[i]
            right = right * nums[i]  # Keeps tracking of product of everything so far from right.

        return res


