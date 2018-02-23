class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        Rotate an array of n elements to the right by k steps.
        For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

        Keep taking first element, delete the first element, then stick the value into end of the array.
        """
        rotateCount = k % len(nums)
        for _ in range(len(nums) - rotateCount):
            nums.append(nums[0])
            del nums[0]

    def rotate_reverse(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        Rotate an array of n elements to the right by k steps.
        For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

        Keep taking first element, delete the first element, then stick the value into end of the array.
        """
        self.reverse(nums,0,len(nums))
        self.reverse(nums,0,k)
        self.reverse(nums,k,len(nums))

    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end-1] = nums[end-1],nums[start]
            start+=1
            end-=1



