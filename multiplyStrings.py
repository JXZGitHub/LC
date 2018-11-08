class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        Time: O(num1*num2)
        Space: O(num1*num2)
        """
        maxLength = len(num1) + len(num2)  # Max length of product of 2 numbers is sum of their length
        res = [0] * maxLength
        startingPos = maxLength - 1  # Shift the starting pos to the left after each round

        # Keep the 'uncarried' raw product at each position and add those products into the final result (with shifting to the left each around), no carrying so far.
        for n2 in range(len(num2) - 1, -1, -1):
            pos = startingPos
            for n1 in range(len(num1) - 1, -1, -1):
                int2 = ord(num2[n2]) - ord('0')
                int1 = ord(num1[n1]) - ord('0')
                prod = int2 * int1
                res[pos] += prod
                pos -= 1
            startingPos -= 1

        # Now 'flatten' the result by figuring out the carry and digit of each position.
        lastCarry = 0
        for p in range(maxLength - 1, -1, -1):
            carry, digit = divmod(res[p] + lastCarry, 10)
            lastCarry = carry
            res[p] = str(digit)

        # Trim leading zeroes, but don't trim the last zero.
        i = 0
        while i < len(res) - 1 and res[i] == '0':
            i += 1
        return ''.join(res[i:])

class Solution_slower:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        rows = []
        maxLength = len(num1) + len(num2)
        res = [0] * maxLength
        startingPos = maxLength - 1
        for n2 in range(len(num2) - 1, -1, -1):
            lastCarry = 0
            row = [0] * maxLength
            pos = startingPos
            for n1 in range(len(num1) - 1, -1, -1):
                int2 = ord(num2[n2]) - ord('0')
                int1 = ord(num1[n1]) - ord('0')
                carry, digit = divmod(int2 * int1 + lastCarry, 10)
                lastCarry = carry
                row[pos] = digit
                pos -= 1

            if lastCarry:
                row[pos] = lastCarry

            rows.append(row)
            startingPos -= 1

        lastCarry = 0
        for p in range(maxLength - 1, -1, -1):
            currSum = 0
            for r in rows:
                currSum += r[p]
            carry, digit = divmod(currSum + lastCarry, 10)
            lastCarry = carry
            res[p] = str(digit)

        finalRes = []
        i = 0
        while i < len(res) - 1 and res[i] == '0':
            i += 1

        finalRes = res[i:]
        return ''.join(finalRes)




sol = Solution()
print (sol.multiply('9','0'))