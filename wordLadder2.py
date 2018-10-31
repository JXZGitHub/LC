import collections
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]

        1) BFS starting at beginWord by transforming every letter to see if the next word is in the wordList, if so, put in queue.
        2) During BFS, maintain a graph of {word:nextWord} for all valid next wods
        3) When a nextWord reaches endWord, do a backtracking DFS (pre-order traversal) on the graph to get all paths.

        Time: O(26*L*N + N), where L is average length of each word, and N is the number of words in the wordList.
        Worst case here is every word transformed happens to be in the list, so each transformation needs 26 * length of word.
        The DFS part is O(N).

        Space: O(N)

        """
        wordListSet = set(wordList + [beginWord])
        graph = collections.defaultdict(list)
        q = set([beginWord])
        count = 0
        result = []
        while q:
            count += 1
            newQ = set()
            for word in q:
                wordListSet.remove(word)
            for word in q:
                if word == endWord:
                    self.getAllPaths(graph, beginWord, endWord, result, [])
                    return result
                for i in range(len(word)):
                    for sub in 'abcdefghijklmnopqrstuvwxyz':
                        if sub != word[i]:
                            newWord = word[:i] + sub + word[i + 1:]
                            if newWord in wordListSet:
                                graph[word].append(newWord)
                                newQ.add(newWord)
            q = newQ
        return []

    def getAllPaths(self, graph, node, target, result, output):
        # This is just a backtracking pre-order traversal DFS on a DAG.
        output.append(node)
        if node == target:
            result.append(output[:])
        else:
            for child in graph[node]:
                self.getAllPaths(graph, child, target, result, output)
                output.pop()


sol = Solution()
print (sol.findLadders("hit","cog", ["hot","dot","dog","lot","log","cog"]))