from collections import defaultdict
class Solution_DFS:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        Example:
        Given a / b = 2.0, b / c = 3.0.
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
        return [6.0, 0.5, -1.0, 1.0, -1.0 ]

        equations = [ ["a", "b"], ["b", "c"] ],
        values = [2.0, 3.0],
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

        Graph + Recursive DFS:

        Build a graph whose nodes are each member of equations, and edge weight is the value,
        and build the reverse connection between each pair where edge weight is 1/value.

        For a given query eg (a,c), search for a existing path in the graph from a to c and keep multiplying
        the edge weight until it reaches c. If path does not exist (cycles back to end or in an unknown node)
        , then it's not found (return -1.0), otherwise the return the total product of each connected node.

        Time: O(e + q*e)
        Space: O(e)

        """
        graph = defaultdict(list)
        res = []
        for (eq1, eq2), val in zip(equations, values):
            graph[eq1].append((eq2, val))
            graph[eq2].append((eq1, 1.0 / val))

        for (q1, q2) in queries:
            seen = set()
            result = self.dfs(q1, q2, graph, seen, 1.0)
            if result is None:
                result = -1.0
            res.append(result)

        return res

    def dfs(self, start, end, graph, seen, value):
        if start in seen or start not in graph or end not in graph:
            return None
        if start == end:
            return value
        seen.add(start)
        neighbors = graph.get(start, [])
        for n in neighbors:  # n is a tuple of (node, value)
            res = self.dfs(n[0], end, graph, seen, n[1] * value)
            if res is not None:
                break
        return res


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        Using Union+Find
        """
        parents = {}  # {Child:Parent}, eg {'a':'b'}
        weights = {}  # {Node: float}, eg{'a': 1.0}
        result = []

        for (eq1, eq2), value in zip(equations, values):
            if eq1 not in parents:
                parents[eq1] = eq1
                weights[eq1] = 1.0
            if eq2 not in parents:
                parents[eq2] = eq2
                weights[eq2] = 1.0
            self.union(eq1, eq2, parents, weights, value)

        for q1, q2 in queries:
            if q1 not in parents or q2 not in parents:
                result.append(-1.0)
            else:
                parent1 = self.find(q1, parents, weights)
                parent2 = self.find(q2, parents, weights)
                result.append(weights[q1] / weights[q2])

        return result

    def union(self, node1, node2, parents, weights, value):
        parent1 = self.find(node1, parents, weights)
        parent2 = self.find(node2, parents, weights)
        if parent1 != parent2:
            parents[parent1] = parent2
            weights[parent1] = value * weights[node2]/weights[node1]

    def find(self, node, parents, weights):
        # Find parent node of a given node, doing path compression while doing so (set the node's parent to its root and update all weights along the way.)
        if parents[node] != node:
            p = parents[node]
            parents[node] = self.find(parents[node], parents, weights)
            weights[node] = weights[node] * weights[p]
        return parents[node]

sol = Solution()
print (sol.calcEquation([["a","b"],["e","f"],["b","e"]],
[3.4,1.4,2.3],
[["a","f"]]))

