import collections
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        Time: O(Max(a,b))
        Space: O(1)
        """
        carry = 0
        res = collections.deque()
        for i in range(max(len(a),len(b))):
            val = carry  #Initialize value of current position with previously generated carry
            if i < len(a):
                val += int(a[-(i+1)]) #Start with the last digit
            if i < len(b):
                val += int(b[-(i+1)]) #Start with the last digit
            carry = val // 2
            val = val % 2 #or: carry,val = divmod(val,2)
            res.appendleft(str(val))
        if carry:
            res.appendleft(str(carry))
        return res[::-1]