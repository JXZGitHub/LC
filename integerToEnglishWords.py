class Solution(object):
    suffix = ['', 'Thousand', 'Million', 'Billion']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', "Eighty", 'Ninety']
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str

        Keep finding the remainder of num // 1000 (ie: num % 1000), and send that as input to a recursive helper function
        that translates any number < 1000 to words, by breaking that number into 0, <20, <100, and else.
        For every returned value of that helper function, append it by the current 'level' (thousand, million, billion)
        to the LEFT of the existing results.
        """
        if num == 0:
            return 'Zero'
        res = ''
        i = 0
        while num > 0:
            num, remainder = divmod(num, 1000)
            if (remainder > 0):
                res = self.parseLessThan1Thousand(remainder) + self.suffix[i] + ' ' + res
            i += 1

        return res.strip()

    def parseLessThan1Thousand(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.less_than_20[num] + ' '
        elif num < 100:
            return self.tens[num // 10] + ' ' + self.parseLessThan1Thousand(num % 10)
        else:
            return self.less_than_20[num // 100] + ' Hundred ' + self.parseLessThan1Thousand(num % 100)

sol = Solution()
print (sol.numberToWords(50868))


