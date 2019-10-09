class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s  # If p is empty, s has to be empty to match
        elif len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or ( (bool(s) and (s[0] == p[0] or p[0] == '.')) and self.isMatch(s[1:], p) )
        else:
            return bool(s) and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
class Solution2:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        # p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for j in range(2, n + 1):
            f[0][j] = p[j - 1] == '*' and f[0][j - 2];

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    f[i][j] = f[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    f[i][j] = f[i][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and f[i - 1][j])

        return f[m][n]


sol = Solution()
print (sol.isMatch('a','a*'))
