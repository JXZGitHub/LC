class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        Time: O(n * 2^n) #For each increasing interval between index 0 to n-1 in s,
        it either should be included or not, so there are 2^n ways. And each way needs check O(n) for palindrome.

        Space: O(n) on stack. O(n) on heap.
        """
        res = []
        self.recurse(s, [], 0, res)
        return res

    def recurse(self, s, output, start, res):
        if start == len(s):
            res.append(output[:])
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                output.append(s[start:i + 1])
                self.recurse(s, output, i + 1, res)
                output.pop()

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True