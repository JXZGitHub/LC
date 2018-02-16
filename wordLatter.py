from collections import deque


class Solution:
    """
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    For example,

    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

    Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

    """
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = deque()
        length = {beginWord: 0}
        q.append(beginWord)
        #    visited = set([beginWord])
        wordListSet = set(wordList)
        while q:
            word = q.popleft()
            if word == endWord:
                return length[word] + 1
            for i in range(len(word)):
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + l + word[i + 1:]
                    if newWord in wordListSet and newWord not in length:
                        q.append(newWord)
                        length[newWord] = length[word] + 1
        return 0
