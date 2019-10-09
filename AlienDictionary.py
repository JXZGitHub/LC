import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        for w in words:
            for c in w:
                graph[c] = []  # Must include every letter in the final result.

        for i, w in enumerate(words):
            if i > 0:
                self.updateGraph(graph, words[i - 1], w)  # Extract a single rule from a pair of words

        res = collections.deque()
        visited = {}

        for node in graph:
            if visited.get(node) != 'Permanent':
                if not self.topoSort(node, graph, visited, res):
                    return ''

        return ''.join(res)

    def topoSort(self, node, graph, visited, res):
        if visited.get(node) == 'P':
            return True
        if visited.get(node) == 'T':
            return False
        visited[node] = 'T'
        for child in graph.get(node, []):
            if not self.topoSort(child, graph, visited, res):
                return ''
        res.appendleft(node)
        visited[node] = 'P'
        return True

    def updateGraph(self, graph, w1, w2):
        minLen = min(len(w1), len(w2))
        for i in range(minLen):
            if i == minLen - 1 and w1[i] == w2[i] and len(w1) > len(w2):
                return ''  # Illegal: First word is longer than 2nd but everything matches so far.
            if w1[i] != w2[i]:
                graph[w1[i]].append(w2[i])
                break


sol = Solution()
print(sol.alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']))
