class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_encoded = {o: i for i, o in enumerate(order)}
        words_encoded = []
        for w in words:
            words_encoded.append([[order_encoded[c]] for c in w])  # [3,4,5],[5,6,7],[9,8], etc

        for i in range(1, len(words_encoded)):
            if words_encoded[i] < words_encoded[i - 1]:
                return False
        return True

sol = Solution()
print (sol.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))