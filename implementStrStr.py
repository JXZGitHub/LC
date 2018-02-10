class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Example 1:

        Input: haystack = "hello", needle = "ll"
        Output: 2
        Example 2:

        Input: haystack = "aaaaa", needle = "bba"
        Output: -1

        """
        h = 0
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        # Only need to check the # of "free-moving" slots: difference between length of haystack and length of needle
        for h in range(len(haystack) - len(needle) + 1):
            for n in range(len(needle)):
                if haystack[h + n] != needle[n]:  # As soon as a mismatch in same position between haystack and needle, don't continue and move t next h in haystack
                    break
            else:
                return h  # If it manages to go through whole length of needle, then success.
        return -1

sol = Solution()
print (sol.strStr('hello','ll'))