class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        Example 1:
        Input: "abc"
        Output: 3
        Explanation: Three palindromic strings: "a", "b", "c".

        Example 2:
        Input: "aaa"
        Output: 6
        Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


        Time: O(N^2)
        Space: O(1)
        """
        count = 0
        for i in range(len(s)):
            count1 = self.isPalindrome(i, i, s)  # Find # of odd-lettered palindromes using a single letter as center
            count2 = self.isPalindrome(i, i + 1,
                                       s)  # Find # of even-lettered palindromes using two letters: single letter + right neighbor as center.
            count += (count1 + count2)
        return count

    def isPalindrome(self, start, end, s):
        """Return number of palindromes using s[start] and s[end] as center, and expanding outward on the 2 sides. As soon as it stops being palindrome, stops expanding and return count
        """
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1

        return count

sol = Solution()
print (sol.countSubstrings('ababa'))