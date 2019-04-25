# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        max_num, max_id = float('-inf'), 0
        for i, n in enumerate(nums):
            if n > max_num:
                max_id = i
                max_num = n

        left_nums = nums[:max_id]
        right_nums = nums[max_id + 1:]

        root = TreeNode(max_num)

        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root

sol = Solution()
print (sol.constructMaximumBinaryTree([3,2,1,6,0,5]))