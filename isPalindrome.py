class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Check if a s is a valid palindrome, case-insensitive, and ignoring non-alphanumeric chars.
        """
        start, end = 0, len(s) - 1
        while (start < end):
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True
