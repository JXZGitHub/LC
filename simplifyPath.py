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
            elif c and c != '.': #Don't add empty chars which can be there due to the .split()
                stack.append(c)
        return '/'+'/'.join(stack) #.join will not add '/' to the end or beginning, so we force it to add in beginnning.


sol=Solution()
print (sol.simplifyPath("/home/"))