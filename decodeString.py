class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        Time: O( max of K * N)
        Space: (N)
        """
        stack = []
        currStr = []
        m = 0
        for c in s:
            if c.isdigit():
                m = m * 10 + int(c)
            elif c not in ('[', ']'):  # Is string
                currStr.append(c)
            elif c == '[':
                stack.append(currStr)
                stack.append(m)
                m = 0
                currStr = []
            elif c == ']':
                prevM = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr * prevM
        return ''.join(currStr)


sol = Solution()
#print (sol.decodeString("3[a2[c]]"))
print (sol.decodeString("3[a]2[bc]"))
#print (sol.decodeString("2[abc]3[cd]ef"))