class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Given N, generate all valid strings including N pairs of ().
        Eg: N=3, output:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
        """
        res = []
        self.generateAll(n, n, '', res)
        return res

    def generateAll(self, leftRem, rightRem, string, res):
        ''' leftRem and rightRem represent number of brackets REMAINING.
            string is the current iteration's string, partial unless it makes all the way to the end.
            res = list of valid strings.
        '''
        if leftRem < 0 or rightRem < 0 or leftRem > rightRem:
            #leftRem > rightRem implies there's more closing parens than opening ones, so that's already invalid
            return False
        if leftRem == rightRem == 0:
            #If both sides' symbols are used up, then it has made it and append string to the result.
            res.append(string)
            return True
        #Otherwise, keep adding ( or ) respectively and go deeper.
        self.generateAll(leftRem - 1, rightRem, string + '(', res)
        self.generateAll(leftRem, rightRem - 1, string + ')', res)