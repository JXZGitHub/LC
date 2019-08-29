class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prevMod = {0: -1}  # -1 here is to handle if a running sum starting from firsrt element of array is divisble by k, then that should return True

        runningSum = 0
        mod = 0
        for i, n in enumerate(nums):
            runningSum += n
            if k != 0:
                mod = runningSum % k
            mod = runningSum % k
            if mod in prevMod:
                prevIndex = prevMod[mod]
                if (i - prevIndex > 1):
                    return True
            else:
                prevMod[mod] = i
        return False
sol = Solution()
print (sol.checkSubarraySum([23, 2, 4, 6, 7],6))