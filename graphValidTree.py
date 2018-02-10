class Solution:
    #Use 'find' and 'union' of disjoint subset, once any 2 edge belongs to same subset, return False.
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nums = [-1 for _ in range(n)]
        for edge in edges:
            subsetA = self.findSubset(nums,edge[0])
            subsetB = self.findSubset(nums,edge[1])
            if subsetA==subsetA: #Two vertices(nodes) are in the same subset, cycle detected!
                return False
            else:
                nums[subsetA] = subsetB #union the two different subsets.
        return len(edges) == n-1

    def findSubset(self, nums, node):
        if nums[node] == -1:
            return node
        return self.findSubset(nums,nums[node])