# Time:  O(n * l^2)
# Space: O(n)

# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        wordLength = len(s)
        # DP[i] = True means if s[:i] can be broken into words in wordDict.
        dp = [False for _ in range(wordLength+1)]
        dp[0] = True #Empty string is always in wordDict.

        for i in range(1,wordLength+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict: #Remember dp starts with 0, so dp[i] corresponds to s[i-1]
                    dp[i] = True
                    break

        return dp[-1]

print (Solution().wordBreak("leetcode", ["leet", "code"]))