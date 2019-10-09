import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int

        Time: O(log(dividend))
        Space: O(1)
        """
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend = math.fabs(dividend)
        divisor = math.fabs(divisor)

        if dividend < divisor:
            return 0

        result = self.longDiv(dividend, divisor)
        # Handles integer overflow (not applicable in python)
        if result >= 2 ** 31 and sign == 1:
            result -= 1
        if sign == -1:
            result = 0 - result
        return result

    def longDiv(self, dividend, divisor):
        if dividend < divisor:
            return 0

        summed = divisor
        m = 1
        while summed * 2 < dividend:
            summed *= 2
            m *= 2
        return m + self.longDiv(dividend - summed, divisor)


sol = Solution()
print (sol.divide(-2147483648,-1))