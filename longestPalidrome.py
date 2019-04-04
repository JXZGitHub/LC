class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Time: O(N^2)
        Space: O(1)
        """
        start = end = 0 #left and right index boundaries of the current longest palindrome,
                        #starting from beginning as center.

        for i, c in enumerate(s):
            #Find palindrome lengths with single and two-letter as center. (i or i+1)
            #Shortest is 0 (ie double letter not a palindrome), single letter minimum length is 1.
            oddPalindromeLength = self.palindromeLengthAroundCenter(s, i, i)
            evenPalindromeLength = self.palindromeLengthAroundCenter(s, i, i + 1)

            #Find the longer of the two palindromes.
            palindromeLength = max(evenPalindromeLength, oddPalindromeLength)

            #If latest palindrome length is longer than the previous one (end-start+1)
            if palindromeLength > (end - start + 1):
                start = i - (palindromeLength - 1) // 2 #shift start to the left boundary of the palindrome
                end = i + palindromeLength // 2         #shift end to the right boundary of the palindrome

        return s[start:end + 1]

    def palindromeLengthAroundCenter(self, s, l, r):
        #Returns the length of the longest possible palindrome inside s,
        #with l and r as left and right index boundaries of the CENTRE (either odd or even center)
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        return r - l - 1 #xABBAy, where l is 0, r is 5. so length of palindrome ABBA should be 5-0-1=4.

s = Solution()
print (#s.longestPalindrome('abba'),
       #s.longestPalindrome('a'),
       #s.longestPalindrome('aa'),
       s.longestPalindrome('xababady'))
       #s.longestPalindrome('') )