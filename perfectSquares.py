class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        Time: O((sqrt(1) + sqrt(2) + sqrt(3) + ... sqrt(N)) #This is approx between N and N^2
        Space: O(N)

        DP:
        dp[0] = 0
        dp[1] = dp[0]+1 = 1
        dp[2] = dp[1]+1 = 2
        dp[3] = dp[2]+1 = 3
        dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 }
              = Min{ dp[3]+1, dp[0]+1 }
              = 1
        dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 }
              = Min{ dp[4]+1, dp[1]+1 }
              = 2						.
        dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
        """
        if n<=3:
            return n
        dp = [ 0,1,2,3 ]
        for i in range(4,n+1):
            minimum = float('inf')
            j = 1
            while (i-j*j>=0): #This runs approx sqrt(i) times.
                minimum = min(minimum,dp[i-j*j]+1)
                j+=1
            dp.append(minimum)
        return dp[n]

sol = Solution()
print (sol.numSquares(13))