class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        Time: O(n)
        Space: O(n)
        """
        stack = []
        res = ''
        temp_res = ''
        m = 0
        for i in s:
            if i.isdigit():
                m = m * 10 + int(i)
            elif i not in ('[', ']'):
                temp_res += i
            elif i == '[':
                stack.append(temp_res)
                stack.append(m)
                temp_res = ''  # Reset
                m = 0  # Reset
            elif i == ']':
                prev_m = stack.pop()
                prev_res = stack.pop()
                res = prev_res + temp_res * prev_m
                temp_res = res  # Do not reset temp_res until a ']' is seen
        return temp_res  # Takes care of single letters


sol = Solution()
#print (sol.decodeString("3[a2[c]]"))
print (sol.decodeString("3[a]2[bc]"))
#print (sol.decodeString("2[abc]3[cd]ef"))