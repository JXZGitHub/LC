class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        Given numRows, generate the first numRows of Pascal's triangle.
        For example, given numRows = 5,
        Return
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
        """
        triangle = []
        for n in range(numRows):
            row = [None for _ in range(n + 1)]
            # The first and last row elements are always 1.
            row[0], row[-1] = 1, 1
            for i in range(1, len(row) - 1):
                # Each triangle element is equal to the sum of the elements
                # above-and-to-the-left and above-and-to-the-right.
                row[i] = triangle[n - 1][i - 1] + triangle[n - 1][i]
            triangle.append(row)
        return triangle