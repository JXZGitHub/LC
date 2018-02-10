class Solution(object):
    #Allows multiple buy and sells
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy_price = sell_price = prices[0]
        profit = 0
        i = 0
        while i < len(prices) - 1:
            while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                i += 1
            buy_price = prices[i]
            while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                i += 1
            sell_price = prices[i]
            profit += sell_price - buy_price

        return profit

sol = Solution()
print (sol.maxProfit([2,1]))

class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i]) #Just adds ALL profit from any two consecutive prices.
        return profit
