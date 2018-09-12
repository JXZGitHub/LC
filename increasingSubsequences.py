class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time: O(n*2^n)
        Space: O(n)
        """
        res = []
        self.recurse(nums, 0, res, [])
        return res

    def recurse(self, nums, index, res, output):
        if len(output) >= 2:
            res.append(output[:])
        seen_in_same_iteration = set()
        for i in range(index, len(nums)):
            if (not output or nums[i] >= output[-1]) and nums[i] not in seen_in_same_iteration:
                output.append(nums[i])
                seen_in_same_iteration.add(nums[i])
                self.recurse(nums, i + 1, res, output)
                output.pop()
