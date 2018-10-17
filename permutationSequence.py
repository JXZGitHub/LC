import math
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str

        Time: O(N^2)
        Space: O(N)
        """
        n_seq = [i for i in range(1, n + 1)]  # 5 -> [1,2,3,4,5]

        k -= 1
        res = []
        for i in range(1, n + 1):
            fact = math.factorial(n - i)
            index = k // fact
            res.append(str(n_seq[index]))
            del n_seq[index]
            k -= index * fact

        return ''.join(res)


class Solution_brute_force:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        return self.recurse([], {}, n, 0, k)[0]

    def recurse(self, output, visited, n, count, k):
        if len(output) == n:
            count += 1
            if count == k:
                return ''.join(output), count
            else:
                return None, count
        else:
            for i in range(1, n + 1):
                if not visited.get(i):
                    output.append(str(i))
                    visited[i] = True
                    res, count = self.recurse(output, visited, n, count, k)
                    if res:
                        return res, count
                    visited[i] = False
                    output.pop()
            return res, count