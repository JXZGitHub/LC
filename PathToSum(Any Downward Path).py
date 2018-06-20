class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time: O(n)
        Space: O(n^2) worst case, O(logn) balanced tree, which is just height of the tree.
        """
        if not root:
            return 0
        return self.pathFromSum(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathFromSum(self, root, sum):
        if not root:
            return 0
        currPathCount = 1 if root.val==sum else 0
        return currPathCount  + self.pathFromSum(root.left, sum-root.val) + self.pathFromSum(root.right, sum-root.val)

from collections import defaultdict
class Solution2:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time: O(n)
        Space: O(n^2) worst case, O(logn) balanced tree, which is just height of the tree.
        """
        cache = defaultdict(int)
        cache[0] = 1
        return self.helper(root, 0, sum, cache)

    def helper(self, root, so_far, sum, cache):
        if root:
            complement = root.val + so_far - sum
            result = cache.get(complement, 0)
            cache[root.val + so_far] += 1
            result += self.helper(root.left, so_far + root.val, sum, cache) + \
                      self.helper(root.right, so_far + root.val,sum, cache)
            cache[root.val + so_far] -= 1
            return result
        else:
            return 0