class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

        For example,
        S = "ADOBECODEBANC"
        T = "ABC"
        Minimum window is "BANC".
        Note:
        If there is no such window in S that covers all characters in T, return the empty string "".

        If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

        """
        start,curr = 0,0
        seen = set()
        min_len=float('inf')
        min_s = ''
        while curr<len(s):
            if s[curr] in t:
                seen.add(s[curr])
            if seen == set(t):
                if curr-start+1 < min_len:
                    min_len = curr-start+1
                    min_s = s[start:curr+1]
                start = curr+1
                seen.clear()
            elif not seen:
                start +=1
            curr+=1
        return min_s