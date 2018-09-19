import collections
class Solution_DFS:
    def countComponents(self, n, edges):
        """
            :type n: int
            :type edges: List[List[int]]
            :rtype: int

            Time: O(N+E)
            Space: Stack O(max # of connected edges). Heap O(N)
        """
        graph = collections.defaultdict(list)
        visited = set()
        res = 0
        for (a, b) in edges:
            graph[a].append(b)
            graph[b].append(a)

        for node in range(n):
            if node not in visited:
                res += 1
                self.traverse(node, graph, visited)
        return res

    def traverse(self, n, graph, visited):
        if n in visited:
            return
        visited.add(n)
        for child in graph.get(n, []):
            self.traverse(child, graph, visited)


class Solution_UF:
    def countComponents(self, n, edges):
        """
            :type n: int
            :type edges: List[List[int]]
            :rtype: int

            Time: O(N)
            Space: O(N)
        """
        parents = {}
        rank = {}
        for (a, b) in edges:
            pA = self.find(a, parents)
            pB = self.find(b, parents)
            if pA != pB:
                ##Union by rank , parent (set) with smaller rank joins bigger rank.
                rA = rank.setdefault(pA, 0)
                rB = rank.setdefault(pB, 0)
                if rA == rB:
                    rank[pB] = rB + 1  # Two sets with same ranks joined, resulting set has +1 rank.
                elif rA > rB:  # Ensures that smaller rank joins bigger rank.
                    pA, pB = pB, pA

                parents[pA] = parents[pB]
        res = set()

        for node in range(n):
            res.add(self.find(node, parents))

        return len(res)

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]