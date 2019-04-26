class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Time: O(N^2)
        Space: O(1)
        """
        maxLen = 0
        start = 0
        end = 0
        for i in range(len(s)):
            start, maxLen = self.fromCenter(i, i, start,end,maxLen,s)
            start, maxLen = self.fromCenter(i, i+1, start,end,maxLen,s)
        return s[start:start+maxLen]

    def fromCenter(self, left, right, start, end, maxLength, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right-left-1 > maxLength:
            return left+1, right-left-1 #A longer palin is found, returns a updated start of this palin, and its length.
        else:
            return start, maxLength #Else, keep returning the existing ones.

s = Solution()
print (#s.longestPalindrome('abba'),
       #s.longestPalindrome('a'),
       #s.longestPalindrome('aa'),
       s.longestPalindrome('xababady'))
       #s.longestPalindrome('') )