import heapq
import math

class Solution:
    """
    Time: O(N*Log(K))
    Space: O(1)
    """
    def kClosest(self, points, K):
        heap = []
        result = []
        for x, y in points:
            diag = math.sqrt(x ** 2 + y ** 2)
            if len(heap) < K:
                heapq.heappush(heap, (-diag, x, y))
            else:
                top = -heap[0][0]
                if diag < top:
                    heapq.heapreplace(heap, (-diag, x, y))

        for h in heap:
            result.append((h[1], h[2]))

        return result


class Solution2(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pivotIndex = len(points) // 2
        pivot = self.dist(points[pivotIndex][0], points[pivotIndex][1])
        nums1, nums2 = [], []
        for i, (x, y) in enumerate(points):
            d = self.dist(x, y)
            if i != pivotIndex and d <= pivot:
                nums1.append([x, y])
            elif d>pivot:
                nums2.append([x, y])

        if len(nums1) + 1 == K:
            return nums1 + [[points[pivotIndex][0], points[pivotIndex][1]]]
        elif len(nums1) < K:
            return self.kClosest(nums2, K - len(nums1) - 1)
        else:
            return self.kClosest(nums1, K)

    def dist(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

sol = Solution2()
print (sol.kClosest([[-2,10],[-4,-8],[10,7],[-4,-7]],3))