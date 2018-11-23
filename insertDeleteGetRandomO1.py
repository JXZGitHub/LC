import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}  # Dictionary maintains key as value to be inserted/deleted, and value as the index for
        # that item in nums list. For deletion, update the lastItem's content to point to the index of the to-be-deleted
        # item, then delete the to-be-deleted-item's key.

        self.nums = []  # Keep appending to this list for every insertion, and for deletion: overwrite the current
        # location of the item with the last item, then pop off the last time.

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        self.nums.append(val)
        self.hashmap[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool

        To remove na existing item, overwrite the location of the item with the content in the last location of the
        array, also re-point the location of the last item in the array to point to the location of the to-be-deleted item, then pop off the last item of the array, and delete the the to-be-deleted item key in dict.

        """
        if val not in self.hashmap:
            return False

        pos = self.hashmap[val]  # Location of the item to be deleted.
        lastItem = self.nums[-1]  # Content of last item

        self.nums[pos] = lastItem  # Overwrite the item to the the last item in the list.
        self.hashmap[lastItem] = pos  # Update hashmap so the last item points to where the deleted item was.

        self.nums.pop()  # Get rid of last item in array, O(1)
        del self.hashmap[val]  # Get rid of last item in dict, O(1)

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomPos = random.randint(0, len(self.nums) - 1)
        return self.nums[randomPos]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()