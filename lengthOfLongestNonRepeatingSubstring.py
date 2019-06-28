class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        length = 0
        left, right = 0,0
        for right,n in enumerate(s):
            if n in seen and seen[n] >= left:
                left = seen[n] + 1 #shift the sliding window's start to be just after the last seen char, only if the last seen one is inside the current sliding window (>= left)
            length = max(length,right-left+1)
            seen[n] = right
        return length

s=Solution()
#print (s.lengthOfLongestSubstring('abba'))
print (s.lengthOfLongestSubstring('xyzabcadxyz'))
#        s.lengthOfLongestNonRepeatingSubstring('abcdeabcdefghijk'),
#        s.lengthOfLongestNonRepeatingSubstring('abc'),
#        s.lengthOfLongestNonRepeatingSubstring('a'),
#        s.lengthOfLongestNonRepeatingSubstring(''))