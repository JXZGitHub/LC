class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int

        Time: O(N^2)
        Space: O(N)

        Input: 3
        Output: 5
        Explanation:
        Given n = 3, there are a total of 5 unique BST's:
       1        3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = self.findDpForLength(dp, i)
        return dp[n]

    def findDpForLength(self, dp, n):
        count = 0
        for i in range(1, n + 1):
            count += (dp[i - 1] * dp[n - i])
        return count

sol = Solution()
print (sol.numTrees(3))
print (sol.numTrees(4))
print (sol.numTrees(10))