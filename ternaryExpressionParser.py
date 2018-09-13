class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str

        Time :O(N)
        Space: O(N)

        Scan expression from right to left, and put every char into stack (except the condition), and once it hits '?', evalluate the local results and put the reuslt back onto stack and continue.
        """
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            e = expression[i]
            if stack and stack[-1] == '?':
                stack.pop()  # Get rid of the '?'
                trueVal = stack.pop()
                stack.pop()  # Get rid of the ':'
                falseVal = stack.pop()
                if e == 'T':
                    stack.append(trueVal)
                else:
                    stack.append(falseVal)
            else:
                stack.append(e)
        return stack[-1]


class Solution_slower:
    """  Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

    Input: "T?2:3"
    Output: "2"

    Input: "F?1:T?4:5"
    Output: "4"
    """

    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str

        Time: O(N^2) ??
        Space: O(1)

        Scan expression from right to left, everytime it hits '?', evalute the local results and modify the expression by substituing the result back, reducing the expression each time until it becomes a single char.
        """
        while len(expression) > 1:
            i = expression.rfind('?')
            c = expression[i - 1]
            trueVal = expression[i + 1]
            falseVal = expression[i + 3]
            val = trueVal if c == 'T' else falseVal
            expression = expression[:i - 1] + val + expression[
                                                    i + 4:]  # Replace evaluated results inside expression, reducing it.

        return expression
