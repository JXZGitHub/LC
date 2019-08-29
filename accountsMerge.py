import collections

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]

        Time: O(N log (N)) <-- all loops except last one is O(N) ( "find" is O(1) due to path compression)
              The last loop with sorting is worst case O(N log (N)), N being the total number of emails.
              Worst case being one big user with all the emails.
              An evenly divided list of emails will be less than N log (N) total.

        Space: O(N), N is total number of emails

        """
        owners = {}
        parents = {}
        merged = collections.defaultdict(set)
        results = []

        #initialize
        for acc in accounts:
            for i in range(1, len(acc)):
                owners[acc[i]] = acc[0] # Map every email to its user
                parents[acc[i]] = acc[i] #Initialize union find data structure to have every node be its own parent

        for acc in accounts:
            p = self.find(acc[1], parents)  # Find parent of the first email in the list.
            for i in range(2, len(acc)):
                # Perform union find on the rest of the emails across all accounts (regardless of account name, as no common email can exist between different names.)
                # Any common emails between any 2 lists will make those 2 lists belong to the same set.
                currP = self.find(acc[i], parents)
                if p != currP:
                    parents[currP] = p

        for acc in accounts:
            p = self.find(acc[1], parents)
            for i in range(1, len(acc)):
                merged[p].add(acc[i])

        for name, emails in merged.items():
            res = [owners[name]] + sorted(emails)
            results.append(res)

        return results

    def find(self, node, parents):
        if node != parents[node]:
            parents[node] = self.find(parents[node], parents)
        return parents[node]




