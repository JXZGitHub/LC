class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        length = 0
        start = 0
        for i,n in enumerate(s):
            if n in seen and seen[n] >= start:
                start = seen[n] + 1 #shift the sliding window's start to be just after the last seen char,
                                    # only if the last seen one is inside the current sliding window (>= start)
            length = max(length,i-start+1)
            seen[n] = i
        return length

s=Solution()
print (s.lengthOfLongestNonRepeatingSubstring('abcdecxyzhmnoabc'),
       s.lengthOfLongestNonRepeatingSubstring('abcdeabcdefghijk'),
       s.lengthOfLongestNonRepeatingSubstring('abc'),
       s.lengthOfLongestNonRepeatingSubstring('a'),
       s.lengthOfLongestNonRepeatingSubstring(''))
