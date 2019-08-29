class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for col in range(len(B[0]))] for row in range(len(A))]  # A is M*N, B is N*P, res = M*P

        for rowA in range(len(A)):
            for colA in range(len(A[rowA])):
                if A[rowA][colA]:
                    for colB in range(len(B[0])):
                        if B[colA][colB]:
                            res[rowA][colB] += A[rowA][colA] * B[colA][colB]
        return res

sol = Solution()
print (sol.multiply([[1,2,3],[4,5,6]], [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]))