class Solution_iterative:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

        Time: O(N)
        Space: O(N) on stack. O(N) on heap.

        Re-usable for Calculator I, II, III.

        Use res to keep track of cumulative results.
        Use one stack to keep track of current result and the sign right after it if '(' is encountered.
        When ')' is seen, pop off the previous results and sign and accumulrate it over the current result
        (which is restarted inside the ())

        Keep track of previous sign and previous number.
        """
        st=[]
        prevSign = '+'
        prevNum = 0
        res = 0
        i=0
        s=s+'+'
        while i<len(s):
            item=s[i]
            if item.isdigit():
                prevNum = prevNum * 10 + int(item)
            elif item in ('+','-'):
                if prevSign == '+':
                    res += prevNum
                elif prevSign == '-':
                    res -= prevNum
                prevNum=0
                prevSign = item
            elif item == '(':
                st.append(res)
                st.append(prevSign)
                res=0
                prevSign='+'
            elif item == ')':
                if prevSign == '+':
                    res += prevNum
                elif prevSign == '-':
                    res -= prevNum
                priorSign = st.pop()
                priorNum = st.pop()
                if priorSign == '+':
                    res = priorNum + res
                elif priorSign == '-':
                    res = priorNum - res
                prevNum = 0
                prevSign = '+'
            i+=1
        return res

sol = Solution_iterative()
print (sol.calculate('1+2-3'))