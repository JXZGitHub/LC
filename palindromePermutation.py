import collections
class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]

        Time: O(N/2*(N/2)!) -> permutation itself is O(N*N!), but we are operating on N/2
        Space: O((N/2)!) on stack. O(N) on heap

        Recursive backtracking:

        Find half of the string, then do regular 'permutation without duplicates' on it,
        and append a MID and a reversed version of the half_string.

        Note:

        eg: 'ababc' --> ab+c+ba, ba+c+ab. c is the mid.

        """
        res = []
        visited = {}

        #keep track of frequency of each letter.
        count = collections.Counter(s)
        odd = 0

        # there can be at most 1 letter that occurs odd number of times to make any palindrome.
        # (ie, aabcc is fine, but aabcdd is not, as existence of 'b' and 'c', each is odd,
        # makes it imposible to make a palindrome as each. No odd occuring letter is ok too.
        for l, c in count.items():
            if c % 2 != 0:
                odd += 1
                if odd > 1:
                    return False
        return True