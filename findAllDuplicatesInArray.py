class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        res = []
        for i, n in enumerate(nums):
            index = abs(n) - 1  # Use the equivalent index of the number's value to check if this number has been seen before.
            if nums[index] < 0:
                res.append(abs(n))
            else:
                nums[index] *= -1  # By negating the value at that index, we can mark whether the index (as a value) has been seen before.
        return res

sol=Solution()
print (sol.findDuplicates([4,3,2,7,8,2,3,1]))