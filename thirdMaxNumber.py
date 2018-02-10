class Solution(object):

    def thirdMax(self, nums):
        #Input: [2, 2, 3, 1]
        #Output: 1
        #Input assumed to be non-empty.
        # Explanation: Note that the third maximum here means the third maximum distinct number.
        # Both numbers with value 2 are both considered as second maximum.
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return sorted(list(set(nums)))[-1]
        else:
            return sorted(list(set(nums)))[-3]


class Solution2(object):
    #Keep 3-member list 'top', to track top 3 numbers seen as you go through each number.
    #Then return the last member of that list.
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = [float('-inf') for _ in range(3)]
        count = 0
        for num in nums:
            if num > top[0]: #Maximum, keep updating it as long as each num is greater than prev
                top[0], top[1], top[2] = num, top[0], top[1]
                count += 1
            elif num != top[0] and num > top[1]: #updating 2nd max, but excludes repeats.
                top[1], top[2] = num, top[1]
                count += 1
            elif num != top[0] and num != top[1] and num > top[2]: #updating max, but excludes repeats.
                top[2] = num
                count += 1

        if count < 3:
            return top[0]

        return top[-1]

sol = Solution2()
print (sol.thirdMax([1,2,4]))