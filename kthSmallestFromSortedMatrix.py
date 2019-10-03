class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        Time: O(log(max(matrix) - min(matrix))*log(n))), where n is number of columns in matrix
        Space: O(1)

        Initially, define 'low' and 'high' as the lowest value and highest value in matrix. then define mid as the middle value between the 2 (may not be a real value in matrix).

        Then using 'right boundary' binary search, count how many items are <= that mid value, and depending on count
        versus k, shrink the range of low and high by either making low = mid+1 or make high=mid.

        Invariant is that kth largest number is always within [low,high], so eventually low becomes > high or high<low,
        and when loop exists, low is the kth largest.

        """
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = matrix[0][0], matrix[rows - 1][cols - 1]
        while low <= high:
            mid = low + (high - low) // 2
            count = 0
            for i in range(rows):
                nums = matrix[i]
                count += self.count(nums, mid)
            if count < k:
                low = mid + 1
            elif count >= k:
                high = mid - 1
        return low

    def count(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = nums[mid]
            if target >= val:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution_heap(object):
    """
    Push the first element of each row into a min heap, while recording its row and col index.
    Then start popping off each element (min) and replace with the next item in its row, do that k times.
    The last popped off element is the kth largest.

    Time: O(k*log(n)), where n is the number of rows in matrix.
    Space: O(n)
    """

    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return ret



