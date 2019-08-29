class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool

        Time: O(len(total chars in all words))
        Space: O(len(total chars in all words))

        """
        order_dict = {}

        for i, n in enumerate(order):
            order_dict[n] = i  # O(len(order))

        words_value = [[order_dict[c] for c in w] for w in words]  # O(len(total chars in all words))
        # convert each word into a list of 'ordering' value: ['apple','app'] => [[1,2,3,4,5],[1,2,3]]

        for i, w in enumerate(words_value[1:], 1):  # O(len(total chars in all words))
            if w < words_value[i - 1]:
                return False
        return True



