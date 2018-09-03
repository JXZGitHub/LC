from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 4, [[1,0],[2,0],[3,1],[3,2]]

        graph = {k:[] for k in range(numCourses)}
        visited = {}
        totalOrder = deque()
        for child, parent in prerequisites:
            graph[parent].append(child)  # parent->children

        for node in graph.keys():
            if visited.get(node) != 'P':
                if not self.topologicalSort(graph, visited, node, totalOrder):
                    return []

        return list(totalOrder)

    def topologicalSort(self, graph, visited, startNode, totalOrder):
        if visited.get(startNode) == 'P':
            return True
        if visited.get(startNode) == 'T':  # cycle!
            return False
        visited[startNode] = 'T'
        for child in graph[startNode]:
            if not self.topologicalSort(graph, visited, child, totalOrder):
                return False

        visited[startNode] = 'P'
        totalOrder.appendleft(startNode)
        return True

sol = Solution()
print (sol.findOrder(2,[[1,0]]))