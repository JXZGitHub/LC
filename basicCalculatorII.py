class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return "0"
        num, stack, sign = 0, [], "+"
        s += ' '
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
        return sum(stack)

sol = Solution()
print (sol.calculate('10-5'))