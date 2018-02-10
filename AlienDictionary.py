from collections import deque
class Solution(object):
    '''
    0) Go through each word in order, and build a DAG (Direct acyclic graph),
       where each node is a letter, and edge betewwen u->v means u comes before v.
    2) Perform a DFS based Topological sort on the graph.
    '''

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, children = set(), {}
        for i in range(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            children[node] = []
        for i in range(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and \
                    words[i - 1][:len(words[i])] == words[i]:
                return "" #Finds invalid sorting

            self.findChildren(words[i - 1], words[i], children)

        # Output topological order by DFS.
        result = deque()
        visited = {}
        for node in nodes:
            if visited.get(node) != 'Permanent':
                if not self.topSortDFS(node, children, visited, result):
                    return ''

        return ''.join(result)


    # Construct the graph, by finding first differt pair of letters in 2 neighboring words in ordering.
    def findChildren(self, word1, word2, children):
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if word1[i] != word2[i]:
                children[word1[i]].append(word2[i])
                break

    # Topological sort, return True with sorting in results if no cycle. Otherwise return True
    def topSortDFS(self, node, children, visited, result):
        if visited.get(node) == 'Permanent':
            return True
        if visited.get(node) == 'Temporary': #Cycle detected
            return False
        visited[node] = 'Temporary'
        for childNode in children[node]:
            if not self.topSortDFS(childNode,children,visited,result):
                return False

        visited[node] = 'Permanent'
        result.appendleft(node)
        return True

sol = Solution()
print (sol.alienOrder(['wrt','wrf','er','ett','rftt']))