class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Keeps 2 pointers, i and p, keep moving i forward until it hits non-zero, then swap with previous pointer (p),
        #after each swap,  move p forward once.
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[pos] = nums[pos],nums[i] #If pos is behind i, then nums[pos] must be a zero awaiting to be switched with a non-zero
                pos +=1