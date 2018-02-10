from collections import Counter
from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        Input:
        "tree"

        Output:
        "eert"

        Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
        """
        return ''.join([char*cnt for char,cnt in Counter(s).most_common()])

class Solution2(object):
    def frequencySort(self, s):
        count = defaultdict(int)
        freq = ["" for _ in range(len(s) + 1)]
        result = ''
        for c in s:
            count[c] += 1
        for char, cnt in count.iteritems():
            freq[cnt] += cnt * char
            #eg: ['','a','aabb','ccc','dddeee']. Index of the 'freq' list is the char count.
            # Could have multiple chars for a given count, so append them as char*number of times.

        for chars in reversed(freq): #Go through 'freq' list with largest first
            result += chars
        return result