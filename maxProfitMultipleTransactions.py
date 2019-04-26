class Solution(object):
    #Allows multiple buy and sells
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Time: O(N)
        Space: O(1)
        """
        if not prices:
            return 0
        buy_price = sell_price = prices[0]
        profit = 0
        i = 0
        while i <= len(prices) - 2:
            while (i <= len(prices) - 2 and prices[i+1] <= prices[i]):
                i += 1
            buy_price = prices[i]
            while (i <= len(prices) - 2 and prices[i+1] >= prices[i]):
                i += 1
            sell_price = prices[i]  #At the last iteration, if price is going down, then hi equals lo, so you add 0 to profit.
            profit += sell_price - buy_price
        return profit

sol = Solution()
print (sol.maxProfit([2,1]))

class Solution2(object):
    # Time: O(N)
    # Space: O(1)
    def maxProfit(self, prices):
        maxP = 0
        for i in range(0, len(prices) - 1):
            # Just adds ALL profit (greater than 0) from any two consecutive prices.
            if prices[i + 1] > prices[i]:
                maxP += (prices[i + 1] - prices[i])
        return maxP
