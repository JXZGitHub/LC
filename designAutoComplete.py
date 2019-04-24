class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.count = 0
        self.children = {}

class AutocompleteSystem:

    def __init__(self, sentences,  times):
        self.trie = TrieNode()
        self.prefix = ''
        for s, count in zip(sentences, times):
            self.insert(s, count)

    def insert(self, sentence, count):
        root = self.trie
        for c in sentence:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.value = sentence
        root.count += count

    def input(self, c):
        if c == '#':
            self.insert(self.prefix, 1)
            self.prefix = ''
        else:
            self.prefix += c
            start = self.search()
            ret = self.dfs(start)
            return [item[-1] for item in sorted(ret, reverse=True)[:3]]

    def dfs(self,root):
        ret = []
        if root:
            if root.value is not None:
                ret.append([root.count, root.value])
            else:
                for c in root.children.values():
                    ret.extend(self.dfs(c))
        return ret

    def search(self):
        root = self.trie
        for c in self.prefix:
            root = root.children[c]
        return root

sol = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
print (sol.input('i'))
