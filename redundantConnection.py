class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]

        
        """
        parents = {}
        latestRedundancy = []
        for (u, v) in edges:
            uParent = self.find(u, parents)
            vParent = self.find(v, parents)
            if uParent != vParent:
                parents[vParent] = uParent
            else:
                latestRedundancy = [u, v]
        return latestRedundancy

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node

        if parents[node] != node:
            p = parents[node]
            parents[node] = self.find(p, parents)
        return parents[node]