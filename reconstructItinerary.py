import heapq
import collections
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        Time: O(n*log(n))
        Space: Stack: O(V+E),V is # of cities, E is number of tickets.
            Heap: O(N)
        """
        graph = collections.defaultdict(list)
        res = collections.deque()
        for f, t in tickets:
            heapq.heappush(graph[f], t)
        self.topo('JFK', graph, res)
        return list(res)

    def topo(self, node, graph, res):
        children = graph.get(node, [])
        while children:
            child = heapq.heappop(children)
            self.topo(child, graph, res)
        res.appendleft(node)


class Solution_iterative_dfs:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        Time: O(n*log(n))
        Space: Heap: O(N)
        """
        graph = collections.defaultdict(list)
        res = collections.deque()
        stack = ['JFK']

        for f, t in tickets:
            heapq.heappush(graph[f], t)

        while stack:
            if not graph.get(stack[-1]):
                node = stack.pop()
                res.appendleft(node)  # Reached a final node with no more outbound connections.
            else:
                stack.append(heapq.heappop(graph[stack[-1]]))  # Go on DFS with the lexically ordered neighbor.
        return list(res)

    def topo(self, node, graph, res):
        children = graph.get(node, [])
        while children:
            child = heapq.heappop(children)
            self.topo(child, graph, res)
        res.appendleft(node)