import math
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend>0 and divisor<0):
            sign = -1

        dividend = math.fabs(dividend)
        divisor = math.fabs(divisor)

        if dividend == 0 or dividend < divisor:
            return 0

        res = self.longDiv(dividend, divisor)
        if sign == -1:
            res = 0 - res
        return res

    def longDiv(self, dividend, divisor):
        if dividend < divisor:
            return 0
        summed = divisor
        multiple = 1
        while (summed + summed <= dividend):
            summed += summed
            multiple += multiple
        return multiple + self.longDiv(dividend-summed,divisor)


sol = Solution()
print (sol.divide(-2147483648,-1))