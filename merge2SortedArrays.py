class Solution:
    # @param A  a list of integers
    # @param m  an integer, number of values of A that's 'initialized', the rest is empty.
    # @param B  a list of integers
    # @param n  an integer, length of B, number of values of B that's 'initialized', the rest is empty.
    # @return nothing
    def merge(self, A, m, B, n):
        last = m+n-1
        indexA = m-1
        indexB = n-1
        while indexA>=0 and indexB>=0:
            if A[indexA] > B[indexB]:
                A[last] = A[indexA]
                indexA -= 1
            else:
                A[last] = B[indexB]
                indexB -= 1

            last-=1

        while indexB>=0:
            A[last] = B[indexB]
            indexB -=1
            last -=1

