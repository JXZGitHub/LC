from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        #Time O(N). Space O(N) <-- each loop has s string slicing, at the first loop it slices nearly the whole string.
        n = len(s)
        seen = set()
        for i in range(n):
            if s[i] not in s[i + 1:] and s[i] not in seen: #if a given char will not repeat in the future and never repeated before, then it's the one.
                return i
            seen.add(s[i])
        return -1

    def firstUniqChar2(self, s):
        # Build a dict of char:freq, and re-scan s, as soon as a char in s is in dict with value == 1, return the index.
        # Time O(2N). Space O(N)
        count = defaultdict(int)
        for i, c in enumerate(s):
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

    def firstUniqChar3(self, s):
        # build frequency table
        freq = {}
        for i, c in enumerate(s):
            if c not in freq:
                # store [frequency, FIRST appearance's index]
                freq[c] = [1, i]
            else:
                # update frequency
                freq[c][0] += 1
        # find leftmost char with frequency == 1
        # it's more efficient to traverse the freq table
        # instead of the (potentially big) input string
        leftidx = float('+inf')
        for c, (f, i) in freq.items():
            if f == 1 and i < leftidx:
                leftidx = i
        # handle edge case: no unique chars were found
        return leftidx if leftidx != float('+inf') else -1


sol = Solution()
print (sol.firstUniqChar('loveleetcode'))