import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = []
        cache = {}
        if not nums:
            return res
        return self.recurse(nums, 0, S, -1, cache)

    def recurse(self, nums, currSum, S, index, cache):
        if currSum == S and index == len(nums)-1:
            return 1
        elif index == len(nums)-1:
            return 0
        if (currSum,index) in cache:
            return cache[(currSum,index)]
        waysSum = self.recurse(nums, currSum + nums[index], S, index + 1, cache)
        waysSubtract = self.recurse(nums, currSum - nums[index], S, index + 1, cache)
        cache[(currSum,index)] = waysSum + waysSubtract
        return waysSum + waysSubtract

class Solution_dp2:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int

        DP: dp[i][j] = number of ways to reach a sum of j using nums[0] to nums[i-1] numbers.
        So dp[i+1][j] = dp[i][j+nums[i+1]] + dp[i][j-nums[i+1]]

        Two observations:
        1) At any given dp[i], range of sum given nums can be -sum(nums) to +sum(nums).
        2) In reality, because j index can only start with 0, we must represent it as -sum(nums)+offset to +sum(nums)+offset. We let offset be +sum(nums), so we go from j from 0 to 2*offset

        """

        offset = sum(nums)  # Maximum possible value of sum of nums is -offset to +offset.
        if S > offset or S < -offset:
            return 0
        dp = collections.defaultdict(int)

        # Offset is used as a starting point beause index can only start with 0 . So offset is same as 0, offset-1 is -1, offset-2 is -1, etc. So the range of sum's is 0 to 2*offset, which is same as -offset to +offset.
        dp[(0, 0)] = 1  # This means there's 1 way to using no number to add to offset (ie, 0) sum

        for i in range(len(nums)):
            for j in range(-offset, offset + 1):
                # dp[(i+1, j)] += dp[(i, j+nums[i])]
                # dp[(i+1, j)] += dp[(i, j-nums[i])]

                # if (i, j) in dp:  # if previous dp exists
                dp[(i + 1, j + nums[i])] += dp[(i, j)]
                dp[(i + 1, j - nums[i])] += dp[(i, j)]
        return dp[(len(nums), S)]

class Solution_dp:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int

        DP: dp[i][j] = number of ways to reach a sum of j using nums[0] to nums[i-1] numbers.
        So dp[i+1][j] = dp[i][j+nums[i+1]] + dp[i][j-nums[i+1]]

        Two observations:
        1) At any given dp[i], range of sum given nums can be -sum(nums) to +sum(nums).
        2) In reality, not all values in that range may exist.

        """

        maxValue = sum(nums)  # Maximum possible value of sum of nums is -offset to +offset.
        if S > maxValue or S < -maxValue:
            return 0
        dp = collections.defaultdict(int)
        dp[(0, 0)] = 1  # This means there's 1 way to using no number to add to 0 sum

        for i in range(len(nums)):
            for j in range(-maxValue,maxValue+1):
                #keep populating forward
                if (i, j+nums[i]) in dp:
                    dp[(i+1, j)] += dp[(i, j+nums[i])]
                if (i, j-nums[i]) in dp:
                    dp[(i+1, j)] += dp[(i, j-nums[i])]
        return dp[(len(nums), S)]

sol = Solution_dp()
print (sol.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0],0))
sol = Solution_dp2()
print (sol.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0],0))