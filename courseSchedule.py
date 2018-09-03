from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        BFS:
        Time: O(V+E)
        Space: O(V) on heap.
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        count = 0

        for child, parent in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1

        # Add 'starting' nodes (without any incoming edge) to the queue
        for i, n in enumerate(indegree):
            if not n:
                q.append(i)
                count += 1

        # For any node off the queue, if any of its children has no more incoming edge, add to queue to visit and count it as a visited node.
        while q:
            node = q.popleft()
            for child in graph.get(node, []):
                indegree[child] -= 1
                if not indegree[child]:
                    count += 1
                    q.append(child)

        # Only if all nodes are visitable in the graph is this a valid topo sort
        return count == numCourses


class Solution_DFS:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Recursive DFS:
        Time: O(V+E)
        Space: O(Deepest path in the graph) on stack frame. O(V) on heap.
        """
        graph = defaultdict(list)
        visited = {}
        for child, parent in prerequisites:
            graph[parent].append(child)
        for course in range(numCourses):
            if not self.visit(graph, visited, course):
                return False
        return True

    def visit(self, graph, visited, node):
        if visited.get(node) == 'P':  # Seen in a previous iteration, 'Permanently Marked'
            return True
        if visited.get(node) == 'T':  # Seen in the same iteration of DFS, 'Temporaily Marked'
            return False
        visited[node] = 'T'
        for child in graph.get(node, []):
            if not self.visit(graph, visited, child):
                return False
        visited[node] = 'P'
        return True


