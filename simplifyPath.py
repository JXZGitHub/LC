class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

        Time: O(N)
        Space: O(N)
        """
        stack = []
        commands = path.split('/')
        for c in commands:
            if c == '..':
                if len(stack) > 0:
                    stack.pop()
            elif c and c != '.':
                stack.append(c)
        return '/'+'/'.join(stack)


sol=Solution()
print (sol.simplifyPath("/..."))