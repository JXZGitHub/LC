import math
from timeit import default_timer as timer
class Solution:
    def isOneEditDistance_better(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time: O(N)
        Space: (1)
        """
        i = 0
        while i < min(len(s), len(t)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                elif len(s) < len(t):
                    return s[i:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
            i += 1
        return math.fabs(len(s) - len(t)) == 1

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) > 1:
            return False
        edits = 0
        sameLength = False
        if len(s) == len(t):
            sameLength = True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if edits > 1:
                return False
            if s[i] != t[j]:
                edits += 1
                j += 1
                if sameLength:
                    i += 1
            else:
                i += 1
                j += 1
        return edits == 1 if (i == len(s) and j == len(t)) else edits == 0



sol = Solution()

start = timer()
sol.isOneEditDistance('123456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance('123456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance('123456789123456789123456789123456789','133456789123456789123456789123456789x')

sol.isOneEditDistance('124456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance('124456789123456789123456789123456789','123456789123456789123456789123456789x')
sol.isOneEditDistance('124456789123456789123456789123456789','123456789123456789123456789123456789x')

end = timer()
print (end-start)

start = timer()
sol.isOneEditDistance_better('123456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance_better('123456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance_better('123456789123456789123456789123456789','133456789123456789123456789123456789x')

sol.isOneEditDistance_better('124456789123456789123456789123456789','133456789123456789123456789123456789x')
sol.isOneEditDistance_better('124456789123456789123456789123456789','123456789123456789123456789123456789x')
sol.isOneEditDistance_better('124456789123456789123456789123456789','123456789123456789123456789123456789x')
end = timer()
print (end-start)