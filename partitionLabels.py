class Solution:
    """
    Time: O(N)
    Space: O(1) , 26 letters as keys to intervals.
    """

    def partitionLabels(self, S):
        last_position = {}
        results = []
        curr_start, curr_end = 0, 0

        for i, s in enumerate(S):
            last_position[s] = i

        for i, s in enumerate(S):
            curr_end = max(curr_end, last_position[s])
            if i==curr_end:
                results.append(curr_end-curr_start+1)
                curr_start=i+1

        return results

sol=Solution()
print (sol.partitionLabels("abcdacf"))