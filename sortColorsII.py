class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing

    FROM LINTCODE:
    Given an array of n objects with k different colors (numbered from 1 to k),
    sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

    Example
    Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
    """

    def sortColors2(self, colors, k):
        # write your code here
        min = 1
        max = k
        left = 0
        right = len(colors) - 1
        i = 0
        while min < max:
            while i <= right:
                if colors[i] == min:
                    colors[i], colors[left] = colors[left], colors[i]
                    left += 1
                    i += 1
                elif colors[i] == max:
                    colors[i], colors[right] = colors[right], colors[i]
                    right -= 1
                else:
                    i += 1
            i = left
            min += 1
            max -= 1
sol = Solution()
x = [3, 2, 2, 1, 4]
sol.sortColors2(x, 4)
print (x)


