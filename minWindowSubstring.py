import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = collections.Counter(t)
        counter = len(t)
        begin, end = 0, 0
        d = float('inf')
        head = 0
        while end < len(s):
            if t_map.get(s[end], 0) > 0:
                counter -= 1
            if s[end] in t_map:
                t_map[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                if s[begin] in t_map:
                    t_map[s[begin]] += 1
                    if t_map.get(s[begin], 0) > 0:
                        counter += 1
                begin += 1
        if d == float('inf'):
            return ''
        else:
            return s[head:head + d]

sol = Solution()
print (sol.minWindow("AAABC","ABC"))

class Solution2:
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
        Time: O(N), N is length of s
        Space: O(K), K is length of differnet chars of t

        """
        from collections import Counter, defaultdict
        curr_count=defaultdict(int) #curr_count represents a running mapping of {char:occurrences} of the current sliding window.
        expected_count=Counter(t) #Find all counts of all chars in t.
        min_start,min_end=0,0
        min_len=float('inf')
        i,start,cnt=0,0,0
        while i < len(s):
            c=s[i]
            if c in expected_count:
                curr_count[c] += 1
                if curr_count[c]<expected_count[c]:
                    cnt+=1
                if cnt == len(t): #If a given substring matches all occurrences of t (not more).
                    while(s[start] not in expected_count or curr_count[s[start]] > expected_count[s[start]]):
                        #Find its start pos
                        curr_count[s[start]] -=1
                        start +=1
                    #Update this substring's starting/ending pos's and minimum length.
                    if i-start+1<min_len:
                        min_start,min_end=start,i
                        min_len=i-start+1
            i+=1
        return s[min_start:min_end+1] if min_len!=float('inf') else ''