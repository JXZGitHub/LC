class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        start = 0
        end = len(s) - 1
        s_list = list(s)  # string is immutable, so convert to list first.
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1

        return ''.join(s_list) #O(N)

class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1] #O(N)