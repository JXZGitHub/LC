class Solution(object):
    def climbStairsRecursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairsIterative(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0  # dp[i] represents the number of stairs needed to reach ith level.
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]