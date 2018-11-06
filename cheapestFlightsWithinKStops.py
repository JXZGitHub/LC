import collections

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int

        BFS
        Time: O(N^(K-1)), because worst case, between city 1 and city 2, there is a edge from 1 to 2 and 2 to 1.
        So at every node, it can travel to N-1 nodes. So if K = 3, its N*(N-1)*(N-1).
        It's wasting time checking for the round trips.
        """
        # [[0,1,100],[1,2,100],[0,2,500]]
        graph = collections.defaultdict(list)
        for parent, child, value in flights:
            graph[parent].append((child, value))

        q = [(src, 0)]
        stops = 0
        result = float('inf')
        while q:
            newQ = []
            for node, currCost in q:
                if node == dst and stops <= K+1:
                    result = min(result, currCost)
                elif stops <= K+1 and currCost < result:
                    for child, newCost in graph[node]:
                        newQ.append((child, currCost + newCost))
            q = newQ
            stops += 1
        return -1 if result == float('inf') else result


class Solution_DFS:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # [[0,1,100],[1,2,100],[0,2,500]]
        graph = collections.defaultdict(list)
        for parent, child, value in flights:
            graph[parent].append((child, value))
        result = float('inf')
        result = self.traverse(graph, src, dst, 0, K, 0, result)
        return result if result != float('inf') else -1

    def traverse(self, graph, node, dst, stops, K, cost, result):
        if stops <= K + 1:
            if node == dst:
                return cost
            else:
                for child in graph[node]:
                    if cost + child[1] < result:
                        result = self.traverse(graph, child[0], dst, stops + 1, K, cost + child[1], result)
        return result


sol = Solution()
print (sol.findCheapestPrice(
3,
[[0,1,100],[1,2,100],[0,2,500]],
0,
2,
0))
