class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc = False
        dec = False
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                inc = True
            elif A[i] < A[i - 1]:
                dec = True
            if inc and dec:
                return False
        return True

