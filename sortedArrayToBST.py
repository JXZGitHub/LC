# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        #The root of a whole (balanced) tree should start at the midpoint of the array (pivot point), and every thing to the left
        #of the pivot is in left subtree, and right is in right subtree. This is true for every subtree.
        """
        return self.recurse(nums,0,len(nums)-1)

    def recurse(self, sortedList, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(sortedList[start])
        mid = start + ((end - start) // 2)
        parent = TreeNode(sortedList[mid])
        parent.left = self.recurse(sortedList, start, mid - 1)
        parent.right = self.recurse(sortedList, mid + 1, end)
        return parent

        # if not nums:
        #     return None
        # rootIndex = len(nums) // 2
        # root = TreeNode(nums[rootIndex])
        # root.left = self.sortedArrayToBST(nums[:rootIndex])
        # root.right = self.sortedArrayToBST(nums[rootIndex+1:])
        # return root