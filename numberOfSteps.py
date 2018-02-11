class Solution(object):
    def climbStairsRecursive(self, n):
        """
        :type n: int
        :rtype: int
        Recusively find Nth fibonaci.
        Time O(2^N) and Space O(N), N calls at most on the stack frame.
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairsDP(self, n):
                """
                :type n: int
                :rtype: int
                Dynamic programming:  dp[i] represents the number of stairs needed to reach ith level.
                Time O(N) and Space O(N)
                """
                dp = {}
                dp[0] = 0  #
                dp[1] = 1
                dp[2] = 2
                for i in range(3, n + 1):
                    dp[i] = dp[i - 1] + dp[i - 2]

                return dp[n]

    def climbStairsIterative(self, n):
        """
        :type n: int
        :rtype: int

        This is just finding n'th fibonaic, no need to maintain list of size n.
        Time O(N) and Space O(1)
        """
        if n == 0:
            return 0

        prev1 = 1 #Number of ways to reach 1 step
        prev2 = 2 #Number of ways ot reach 2nd step.
        if n == 1:
            return prev1
        if n ==2 :
            return prev2

        for _ in range(3, n + 1):
            prev1,prev2 = prev2, prev1+prev2

        return prev2