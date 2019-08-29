class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node=node.children[w]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, 0, self.trie)  # level initialized to 0 because root of a trie does not have a letter.

    def match(self, word, level, node):
        if level == len(word):
            return bool(node.isWord)
        char = word[level]
        if char in node.children:
            return self.match(word, level + 1, node.children[char])
        if char == '.':
            for c in node.children:
                if self.match(word, level + 1, node.children[c]):
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.value = None
#
#
# class WordDictionary:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = TrieNode()
#
#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: void
#
#         Time: O(N)
#         Space: O(N)
#
#         """
#         node = self.trie
#         for i, w in enumerate(word):
#             if w not in node.children:
#                 node.children[w] = TrieNode()
#             node = node.children[w]
#         node.value = word  # Denotes a leaf
#
#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#
#         Time: O(All letters of all words in Dict).
#         Space: Stack O(len(longest word in the dict))).
#         """
#         return self.match(word, 0, self.trie)
#
#     def match(self, word, level, node):
#         if level == len(word):
#             return bool(node.value)  # Ensure it's a leaf node, to avoid searching for 'b.' when only 'bad' exists and thinking it's a match.
#         if word[level] == '.':
#             # As long as any of its children (sub-trie) has a match for the remaining part of the word
#             for c in node.children:
#                 if self.match(word, level + 1, node.children[c]):
#                     return True
#             return False
#         else:
#             # Otherwise only search for the specific sub-Trie under the right child.
#             return word[level] in node.children and self.match(word, level + 1, node.children[word[level]])

        # Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
print (obj.search('bad'))
