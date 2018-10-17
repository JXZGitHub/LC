class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        DP
        Time: O(len(s)*len(p))
        Space: O(len(s)*len(p))
        """
        #  dp[i][j] = whether s[0...i-1] matches p[0...j-1]
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        # initialize dp to False
        dp[0][0] = True

        # empty pattern mismaches all
        # empty string matches * pattern:
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*' and dp[0][j - 1]:
                dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    # not * or .,  matches any character at current string and as long as previous s and p matches then
                    # current one matches.
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                elif p[j - 1] == '*':
                    # For *, either the current str already matched previous pattern (* matches empty string),
                    # or previous pattern matches current string (* matches whatever char at current position)
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]
