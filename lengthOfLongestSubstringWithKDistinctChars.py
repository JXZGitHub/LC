import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time: O(N)
        Space: O(N)

        Sliding window. Start moving right boundary and tally char frequency and distinct char count. If distinct char > k in a given iteration, start an inner while loop moving left boundary until distinct count becomes <=k again, updating char frequency and distinct too as we shift to the left. Then go back to outerloop and update right boundary again.
        """
        left = 0
        right = 0
        count = collections.defaultdict(int)
        distinct = 0
        res = 0
        while right < len(s):

            # Tally counts of chars in current window.
            c = s[right]
            if count[c] == 0:
                distinct += 1  # Tally distinct chars in current window.
            count[c] += 1

            # Keep sliding the left boundary of window until number of distinct chars in window is again <=k.
            while distinct > k:
                left_char = s[left]
                count[left_char] -= 1  # Reducing the left char's count as we move left.
                if count[left_char] == 0:
                    distinct -= 1  # Update distinct if no more given char left in this window.
                left += 1  # Move window left

            res = max(res, right - left + 1)
            right += 1
        return res

sol = Solution()
print (sol.lengthOfLongestSubstringKDistinct2("eceba",2))
