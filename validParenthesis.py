class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
        string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid
        but "(]" and "([)]" are not.

        Only push opening symbols onto stack, and if a closing symbol is found,
        it must match the whatever is popped off the stack, otherwise, it's not valid.
        """
        stack = []
        parens = {'(': ')', '{': '}', '[': ']'}
        for x in s:
            if x in parens:
                stack.append(x)
            elif not stack or parens.get(stack.pop()) != x:
                return False

        return len(stack) == 0


