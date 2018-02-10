import math
import bisect

class Solution1(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        return sorted(sorted(arr,key=lambda a: math.fabs(a-x))[:k])


class Solution2(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        size = len(arr)
        lo = max(bisect.bisect_right(arr, x) - 1, 0)
        hi = lo + 1
        left = right = lo
        count = 0

        while count < k and (lo >= 0 or hi < size):
            if hi >= size or (lo >= 0 and x - arr[lo] <= arr[hi] - x):
                left = lo
                lo -= 1
            elif lo <= 0 or (hi < size and x - arr[lo] > arr[hi] - x):
                right = hi
                hi += 1
            count += 1

        return arr[left:right + 1]


sol = Solution1()
print (sol.findClosestElements([1,2,3,4,5], 4, 3))

sol2 = Solution2()
print (sol2.findClosestElements([1,2,3,4,5], 4, 3))


