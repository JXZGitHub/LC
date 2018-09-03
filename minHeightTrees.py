from collections import defaultdict


import collections
# from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]

        Time: O(N)
        Space: O(N)
        BFS: Start with all leaves (with only 1 neighbor), and keeping cutting off the leaves, and moving onto the next
        set of leaves, until there are at most 2 nodes remaining. Those 2 nodes (or 1 node) are the results.

        Intuition is that you want to use the most middle-located nodes, which can be one node or 2 nodes
        depending on parity of total nodes
        """
        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = collections.deque([node for node in range(n) if len(graph[node]) == 1])  # Only a single connection means it's a leaf.
        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                l = leaves.pop()
                neighbor = graph[l].pop()
                graph[neighbor].remove(l)  # Prune the leaf
                if len(graph[neighbor]) == 1:  # If after pruning its leave, the neighbor is now also leaf
                    leaves.appendleft(neighbor) #Work on this new generation of leaves in the next iteration.
        return list(leaves)



class Solution_N_Squared:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        minDepth = float('inf')
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = []
        for node in range(n):
            depth = self.bfsMaxDepth(node, None, graph)
            if depth < minDepth:
                result = [node]
                minDepth = depth
            elif depth == minDepth:
                result.append(node)
        return result

    def bfsMaxDepth(self, node, prevNode, graph):

        if graph[node] == [prevNode]:
            return 0  # Reaches leaf.

        maxDepth = float('-inf')
        for child in graph[node]:
            if child != prevNode:
                depth = 1 + self.bfsMaxDepth(child, node, graph)
                maxDepth = max(depth, maxDepth)

        return maxDepth



sol = Solution()
print (sol.findMinHeightTrees(4,([1, 0], [1, 2], [1, 3])))
print (sol.findMinHeightTrees(6,([[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])))
print (sol.findMinHeightTrees(6,([[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]])))