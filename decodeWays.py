class Solution(object):
    """
    A message containing letters from A-Z is being encoded to numbers using the following mapping:
        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Given a non-empty string containing only digits, determine the total number of ways to decode it.

        Example 1:
        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).

        Example 2:
        Input: "226"
        Output: 3
        Explanatio: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

        Time: O(N)
        Space: O(N)
    """

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s) + 1)]  # dp[i] = ways to decode s[i+1].
        dp[0] = 1  # dp has one more element than S to so that DP[0] = 0 ,which means there's 1 way to decode an empty string

        for i in range(1, len(dp)):
            if s[i - 1] == '0':  # No 0 is allowed, so its appearance means 0 way to decode current char.
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]  # No matter what, you have at least as many ways to get decode s[:i] as there are ways to decode its left neighbor.

            # Check previous char (s[i-2]):
            #  1) if previous char is 1, then the s[:i] can be decoded dp[i-1] more ways by taking the last 2 chars (10,11,12,13....), and combining with however many way there are to derive the the 3rd char back (dp[i-2])
            #  2) same idea if previous char is 2 and current is less than  6, you can form (20,21,22...26)
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                dp[i] += dp[i - 2]

        return dp[-1]

sol = Solution()
print (sol.numDecodings('2221'))
print (sol.numDecodings('60'))
print (sol.numDecodings('110'))