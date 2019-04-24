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
