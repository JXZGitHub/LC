# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int

        :rtype: bool

        Time: O(N)
        Space: O(N)

        Does inorder traversal, Keep track of every seen node and check if the remainder is there.
        """
        stack = []
        nums = []
        seen = set()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if k - node.val in seen:
                    return True
                else:
                    seen.add(node.val)
                root = node.right

    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool

        Time: O(N)
        Space: O(N) on heap. O(logN) on stack frame.

        Use inorder traversal to turn tree into sorted array, then use traditional 2 pointer 2 sum to find target.
        """
        stack = []
        nums = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                nums.append(node.val)
                root = node.right

        start, end = 0, len(nums) - 1
        while start < end:
            test = nums[start] + nums[end]
            if test == k:
                return True
            elif test < k:
                start += 1
            else:
                end -= 1
        return False
