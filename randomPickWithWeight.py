import random
class Solution:
    """
    Given a list eg: [1,2,3]. At index 0, weight is 1. Index 1, weight is 2. Index 3 Weight is 3.

    Which means each call of pickIndex should return 0 (index) with probability (1/6),
    return 1 w/ prob (2/6) and return 3 w/ prob 3/6.

    First, create another list of same size, but each element is the cumulative sum at current position of input list.
    [1,2,3] will become [1,3,6]. Then for each pickIndex(), randomly generate between [1,6].
    And then it's doing a Binary 'right boundary' search on the cumulative sum list with target = that random number.
    'Right boundary' is the first element > target, or last element= target.

    """

    def __init__(self, w):
        """
        :type w: List[int]

        Time: O(N)
        Space: O(N)
        """
        self.cumWeights = [w[0]]
        for i in range(1, len(w)):
            self.cumWeights.append(self.cumWeights[i - 1] + w[i])

    def pickIndex(self):
        """
        :rtype: int

        Time: O(log(N))
        Spac: O(1)
        """
        target = random.randint(1, self.cumWeights[-1])
        start, end = 0, len(self.cumWeights) - 1
        index = None
        while start <= end:
            mid = start + (end - start) // 2
            value = self.cumWeights[mid]
            if target >= value:
                start = mid + 1
            elif target < value:
                end = mid - 1
            if target == value:
                index = mid
        if index is not None:
            return index
        else:
            return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,99999])
print (obj.pickIndex())

