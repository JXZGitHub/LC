class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        Matrx A (N*M)
        Matrix B (M*P)
        Matrix AxB = (N*P),
        where each final cell (i,j) is the sum of every ith row of A multiplied by every jth column of B
        Time: O(N*M*P)
        Space: O(N*P)
        """
        #Initialize 0's for the resulting matrix: # of A's rows X # of B's columns.

        res = [ [0 for _ in range(len(B[0]))]
                   for _ in range(len(A)) ]

        for res_row in range(len(A)):
            for colA_rowB in range(len(A[0])): #Go through each column of A (ie, each row of B)
                if A[res_row][colA_rowB]:
                    for res_col in range(len(B[0])): #Go through each column of B
                        if B[colA_rowB][res_col]:
                            #Fill the results's row by row, each row is accumulated (Column of A or Row of B) times.
                            res[res_row][res_col] += A[res_row][colA_rowB] * B[colA_rowB][res_col]
        return res