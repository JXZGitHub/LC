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
                    return res

        mid, half_s = "", []
        for l, c in count.items():
            if c % 2 != 0:
                #mid.append(l) #For any odd occuring letters, make ONE occurence the middle. Then the rest becomes even occuring again.
                mid = l
            for i in range(c // 2):
                half_s.append(l) #Add half of the occurences of each letter.
        self.recurse(half_s, visited, [], mid, res) #perform regular 'permutation without duplicate' on the half letters.
        return res

    def recurse(self, s, visited, output, mid, res):
        if len(output) == len(s): #mid is always a single LETTER or empty string
            res.append(''.join(output) + mid + ''.join(reversed(output)))
        else:
            for i in range(len(s)):
                if visited.get(i) or (i > 0 and s[i] == s[i - 1] and not visited.get(i - 1)):
                    continue
                output.append(s[i])
                visited[i] = True
                self.recurse(s, visited, output, mid, res)
                visited[i] = False
                output.pop()

sol = Solution()
print (sol.generatePalindromes('bcacbca'))
print (sol.generatePalindromes('aabbb'))