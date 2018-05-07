class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if s[0] == '0':
            return 0
        if s[0] == '*':
            dp[1] = 9  # If first char is *, then at last 9 ways.
        else:
            dp[1] = 1

        m = 1e9 + 7
        for i in range(2, len(dp)):
            if s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9  # for a *, at least 9 X previuos encoding ways
                if s[i - 2] == '1':
                    dp[i] += dp[i - 2] * 9  # 11,12,13,...19
                elif s[i - 2] == '2':
                    dp[i] += dp[i - 2] * 6  # 21,22,..26
                elif s[i - 2] == '*':
                    dp[i] += dp[i - 2] * 15  # 11,12,13...19 AND 21,22,....26
            elif int(s[i - 1]) >= 1 and int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]  # There's at least one new way of encoding, just stand alone last digit (1 to 9)
                if s[i - 2] == '1' or (s[i - 2] == '2' and int(s[i - 1]) <= 6):
                    dp[i] += dp[i - 2]  # Same as decode ways I: one additional encoding: 11,12,13,.... or 21,22,...26.
                if s[i - 2] == '*':
                    if int(s[i - 1]) <= 6:
                        dp[i] += dp[i - 2] * 2  # eg, if s[i-1] is 5, then last 2 digits can be 15 or 25.
                    else:
                        dp[i] += dp[i - 2]  # eg, if s[i-1] is 7, then last 2 digits can only be 17.
            elif int(s[i - 1]) == 0:
                if s[i - 2] in ('1', '2'):
                    dp[i] += dp[i - 2]  # eg: 110-> 1,10 (1 way)
                elif s[i - 2] == '*':
                    dp[i] += dp[i - 2] * 2  # eg: 1*0 -> 120, 110 (2 ways)
                else:
                    return 0

            dp[i] = dp[i] % m

        return int(dp[-1])
sol = Solution()
print (sol.numDecodings('*1'))