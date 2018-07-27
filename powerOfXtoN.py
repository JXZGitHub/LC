class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Implement pow(x, n), which calculates x raised to the power n.


        Example 1:

        Input: 2.00000, 10
        Output: 1024.00000

        Example 2:

        Input: 2.10000, 3
        Output: 9.26100

        Example 3:

        Input: 2.00000, -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25

        The idea is that X^N = X^(N/2) * X^(N/2) if N is even (eg: x^8 = x^4 * x^4)
        And X^N = X^(N/2) * X^(N/2) * X if N is odd (eg: x^9 = x^4 * x^4 * x)

        So we do not need to multiply X by X N times to get X^N, only log(N) times.

        time: O(log(N)) #log(N) number of computations.
        space: O(log(N)) #log(N) number of recursive calls on stack frame
        """

        if n < 0:
            return 1.0 / self.power(x, -n)
        return self.power(x, n)

    def power(self, x, n):
        if n == 0:
            return 1
        half = self.power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

class Solution_iterative:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Implement pow(x, n), which calculates x raised to the power n.


        Example 1:

        Input: 2.00000, 10
        Output: 1024.00000

        Example 2:

        Input: 2.10000, 3
        Output: 9.26100

        Example 3:

        Input: 2.00000, -2
        Output: 0.25000
        Explanation: 2-2 = 1/22 = 1/4 = 0.25

        The idea is that X^N = X^(N/2) * X^(N/2) if N is even (eg: x^8 = x^4 * x^4)
        And X^N = X^(N/2) * X^(N/2) * X if N is odd (eg: x^9 = x^4 * x^4 * x)

        So we do not need to multiply X by X N times to get X^N, only log(N) times.

        time: O(log(N)) #log(N) number of computations.
        space: O(log(N)) #log(N) number of recursive calls on stack frame
        """

        if n < 0:
            return 1.0 / self.power(x, -n)
        return self.power(x, n)

    def power(self, x, n):
        res = 1
        i = n
        while (i>0):
            if i % 2 != 0:
                res = res * x
            x = x*x
            i = i // 2
        return res if n>=0 else 1.0/res

sol = Solution_iterative()
print (sol.power(2,8))