class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        dp[i] = min number of coins to make amount i.
        initialize dp of size amount+1 all to amount+1 (impossibly large), with dp[0] = 0: no way to make amount 0.

        Then dp[i] = min(dp[i], dp[i-coin value]+1): the min way to make the remainder (i-coin value)+1
        may be smaller than the current min way (possibly initialized or updated before)

        Time: O(amount * coins)
        Space: O(amount)

        """
        dp = [ amount + 1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i],dp[i-c]+1)
        if dp[amount]>amount:
            return -1
        else:
            return dp[amount]

    def coinChange2(self, coins, amount):
        dp = [int(1e100) for i in range(amount + 1)]
        dp[0]=0
        return self.dfs(coins,amount,dp)

    def dfs(self, coins, target, dp):
        if target<0:
            return -1
        if dp[target] != int(1e100):
            return dp[target]
        for c in coins:
            tmp = self.dfs(coins,target-c, dp)
            if tmp>=0:
                dp[target] = min(dp[target],tmp+1)
        if dp[target] == int(1e100):
            return -1
        else:
            return dp[target]






sol = Solution()
#print (sol.coinChange([1,2,5],11))
print (sol.coinChange2([1,2,5],11))
