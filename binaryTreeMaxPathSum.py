class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int

        1) Max path sum of a node is current node value + the bigger of max path sum of either left or right subtree.
        2) However, at the last level, where the subtree has 2 leaves, the max path sum is total sum of all its values.
        3) If a given node's any subtree has negative path sum, don't add to the max path sum.

        Recursive go all the way to the left then right subtree, keep track of global max path sum as root + left path sum + right path sum.
        BUT, when returning up the recursion (starting from leaf), return root val + max(left path sum ,right path sum). This takes care of           1).

        Time: O(N)
        Space: O(log(N))

        """
        maxSum = [float('-inf')]  # Use a mutable list to keep state of maxSum during recursion, to avoid using a class level variable.
        self.dfs(root, maxSum)
        return maxSum[0]

    def dfs(self, root, maxSum):
        if not root:
            return 0
        leftMaxSum = max(self.dfs(root.left, maxSum), 0) #Don't contribute negative to sum
        rightMaxSum = max(self.dfs(root.right, maxSum), 0)
        maxSum[0] = max(maxSum[0], root.val + leftMaxSum + rightMaxSum)
        return root.val + max(leftMaxSum, rightMaxSum)