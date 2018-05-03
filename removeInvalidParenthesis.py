from collections import deque
class Solution:
    ''' Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
        Note: The input string may contain letters other than the parentheses ( and ).
        Examples:
        "()())()" -> ["()()()", "(())()"]
        "(a)())()" -> ["(a)()()", "(a())()"]
        ")(" -> [""]

        O: n*C(n,n)+(n-1)*C(n,n-1)....+1*C(n,1) = n*2^(n-1).
        Space complexity: same???

    '''
    def valid(self, s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = set()
        res = []
        if not s:
            return res

        q = deque()
        q.append(s)
        found = False
        while q:
            t = q.popleft()
            if self.valid(t):
                res.append(t)
                found = True
            if found:
                continue
            for i, n in enumerate(t):
                if n not in ('(', ')'):
                    continue
                x = t[:i] + t[i + 1:]
                if x not in visited:
                    visited.add(x)
                    q.append(x)
        return res