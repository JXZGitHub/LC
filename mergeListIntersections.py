class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            intA = A[i]
            intB = B[j]

            startMax = max(intA[0], intB[0])
            endMin = min(intA[1], intB[1])

            if not (intA[0] > intB[1] or intB[0] > intA[1]):  # ENsure intervals A and B have some overlap.
                res.append([startMax, endMin])

            # whichever interval ended first, move to its next interval.
            if intA[1] == endMin:
                i += 1
            if intB[1] == endMin:
                j += 1

        return res

