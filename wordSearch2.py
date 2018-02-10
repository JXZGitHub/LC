class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isLeaf = True


class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        visited = [[False for _ in range(len(board[0]))] for i in range(len(board))]
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        results = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.findGivenWord(trie, board, row, col, visited, '', results)

        return list(results)

    def findGivenWord(self, trie, board, row, col, visited, prefix, results):
        if not trie or row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]:
            return

        if board[row][col] not in trie.children:
            return

        if trie.children[board[row][col]].isLeaf:
            results.add(prefix+board[row][col])

        visited[row][col] = True
        self.findGivenWord(trie.children[board[row][col]], board, row + 1, col, visited, prefix + board[row][col],
                           results)
        self.findGivenWord(trie.children[board[row][col]], board, row - 1, col, visited, prefix + board[row][col],
                           results)
        self.findGivenWord(trie.children[board[row][col]], board, row, col + 1, visited, prefix + board[row][col],
                           results)
        self.findGivenWord(trie.children[board[row][col]], board, row, col - 1, visited, prefix + board[row][col],
                           results)
        visited[row][col] = False

sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oat","oath","pea","eat","rain"]
print (sol.findWords(board,words))

