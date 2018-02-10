class Solution:
    def lengthOfLongestNonRepeatingSubstring(self, s):
        #Returns the length of the longest nonrepeating substring in s:
        #eg: 'abcdecxyzhmnoabc' returns 12 ('decxyzhmnoab')
        start = 0
        longest = 0
        letterToIndex = {}
        for i,c in enumerate(s):
            #SLIDING WINDOW:Start accumulating a string beginning with start, until it hits something seen before,
            ## then slide the start to be right after the seen letter.
            if c in letterToIndex: #If a letter has been seen before
                # Adjust start index to right after the seen letter's index, if it's AFTER the current start index
                # If the last seen letter location is BEFORE start, then no need to adjust start.
                start = max(letterToIndex[c]+1,start)
            longest = max(longest, i-start+1)
            letterToIndex[c]=i
        return longest

s=Solution()
print (s.lengthOfLongestNonRepeatingSubstring('abcdecxyzhmnoabc'),
       s.lengthOfLongestNonRepeatingSubstring('abcdeabcdefghijk'),
       s.lengthOfLongestNonRepeatingSubstring('abc'),
       s.lengthOfLongestNonRepeatingSubstring('a'),
       s.lengthOfLongestNonRepeatingSubstring(''))
