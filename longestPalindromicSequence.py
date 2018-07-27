class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int


        Example 1:
        Input:

        "bbbab"
        Output:
        4
        One possible longest palindromic subsequence is "bbbb".
        Example 2:
        Input:

        "cbbd"
        Output:
        2
        One possible longest palindromic subsequence is "bb".

        dp[i][j] is length of longest palindrome subsequence in s[i] to s[j] inclusive.
        so then dp[i][i] = 1, and if dp[i]=dp[j] then dp[i][j] = dp[i+1][j-1] + 2 (if two end points match,
        then whatever palindrome count in between the 2 can be incrememnted by 2 to include the 2 end points.)
        else, dp[i][j] = max(dp[i][j-1], dp[i+1][j]) , which means it is whatever palindrome count is larger by
        removing each end point respectively.

        Time: O(N^2)
        Space: O(N^2)
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # dp = [ [0]*len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            """Why is the outer loop (i) in reverse order?
               dp[i][j] = dp[i+1][j-1], so dp[i][j] depends on calculated value of dp[i+1], 
               which if we didn't reverse order of i, it would not have been calculated yet (defaulted to 0)
            """

            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
sol = Solution()
print (sol.longestPalindromeSubseq('abba'))