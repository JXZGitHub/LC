from collections import deque

class Solution_DFS_Recursive:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool

        Time: O(V+E) #Number of vertices in the graph + number of edges.
        Space: O(max(V) of any  given edge) on stack frame. O(V) on heap.
        """
        nodeColor = {}
        for i in range(len(graph)):
            if i not in nodeColor and not self.recurse(graph, 1, i, nodeColor):
                return False
        return True

    def recurse(self, graph, targetColor, i, nodeColor):
        if i in nodeColor:
            return nodeColor[i] == targetColor
        nodeColor[i] = targetColor
        for neighbor in graph[i]:
            if not self.recurse(graph, -targetColor, neighbor, nodeColor):
                return False
        return True


class Solution_DFS_Iterative:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool

        Time: O(V+E) #Number of vertices in the graph + number of edges.
        Space: O(V)
        """
        nodeColor = {}
        s = []
        for i in range(len(graph)):
            if i in nodeColor:  # A node that is already 'colored' have already been compared with all of its edges, so skip it.
                continue
            nodeColor[i] = 1
            s.append(i)
            while s:
                node = s.pop()
                for neighbor in graph[
                    node]:  # Compare all of its neighbor, either color it if uncolored, or compare if the neighbor is same color as itself.
                    if neighbor not in nodeColor:
                        nodeColor[neighbor] = -nodeColor[node]
                        s.append(neighbor)
                    else:
                        if nodeColor[neighbor] == nodeColor[node]:
                            return False

        return True


class Solution_BFS:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool

        Time: O(V+E) #Number of vertices in the graph + number of edges.
        Space: O(V)
        """
        nodeColor = {}
        q = deque()
        for i in range(len(graph)):
            if i in nodeColor:  # A node that is already 'colored' have already been compared with all of its edges, so skip it.
                continue
            nodeColor[i] = 1
            q.append(i)
            while q:
                node = q.popleft()
                for neighbor in graph[
                    node]:  # Compare all of its neighbor, either color it if uncoored, or compare if the neighbor is same color as itself.
                    if neighbor not in nodeColor:
                        nodeColor[neighbor] = -nodeColor[node]
                        q.append(neighbor)
                    else:
                        if nodeColor[neighbor] == nodeColor[node]:
                            return False

        return True