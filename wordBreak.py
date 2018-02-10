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

        for subStringLength in range(1,wordLength+1):
            for partitionLength in range(1,subStringLength+1):
                if dp[subStringLength-partitionLength] and \
                   s[subStringLength-partitionLength:subStringLength] in wordDict:
                    dp[subStringLength] = True
                    break

        return dp[-1]

print (Solution().wordBreak("leetcode", ["leet", "code"]))