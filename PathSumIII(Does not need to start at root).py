# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Non_linear_time:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time: O(n^2)
        Space: Recusion on stack frame: O(n^2) worst case, O(nlogn) balanced tree
        """
        if not root:
            return 0
        return self.pathFromSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathFromSum(self, root, sum):
        if not root:
            return 0
        currPathCount = 1 if root.val == sum else 0
        return currPathCount + self.pathFromSum(root.left, sum - root.val) + self.pathFromSum(root.right,
                                                                                              sum - root.val)


from collections import defaultdict


class Solution_Linear_Time:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time: O(n)
        Space: Stack frame for recursion: O(n) worst case, O(logn) balanced tree, which is just height of the tree.
               Heap space for prefix sum hashing: O(n)
        """
        seenSum = defaultdict(int)  # A hashmap of { sum seen in a given path : number of times it's been seen }
        seenSum[0] = 1
        return self.recurse(root, 0, sum, seenSum, 0)

    def recurse(self, root, previousSum, targetSum, seenSum, result):
        if not root:
            return 0
        prefixSum = root.val + previousSum - targetSum  # Given the cumulative sum including this node, what must be the sum of all of its parent nodes in this path?
        result = seenSum.get(prefixSum,
                             0)  # And however many times such a prefix sum existed in the path leading up to here, that's the number of possible ways to get to target Sum at this node.
        seenSum[root.val + previousSum] += 1  # Keep track of prefix sum

        result += self.recurse(root.left, root.val + previousSum, targetSum, seenSum, result) + self.recurse(root.right,
                                                                                                             root.val + previousSum,
                                                                                                             targetSum,
                                                                                                             seenSum,
                                                                                                             result)

        seenSum[
            root.val + previousSum] -= 1  # Backtrack back to the root so we need to erase whatever seenSum updates we did when going down the root.

        return result


class Solution_print_all_paths:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time: O(n*log(n)) for balanced tree, O(n^2) for skewed tree.
        Space: Stack frame for recursion: O(n) worst case, O(logn) balanced tree, which is just height of the tree.
               Heap space for prefix sum hashing: O(n)
        """
        seenSum = defaultdict(int)  # A hashmap of { sum seen in a given path : number of times it's been seen }
        seenSum[0] = 1
        result = []
        self.recurse(root, 0, sum, seenSum, [], result)
        return result

    def recurse(self, root, previousSum, targetSum, seenSum, combo, result):
        if not root:
            return
        prefixSum = root.val + previousSum - targetSum  # Given the cumulative sum including this node, what must be the sum of all of its parent nodes in this path?
        combo.append(root.val)

        if seenSum.get(prefixSum,0) > 0:  # Same condition as the original problem: a target sum is definitely contained in this path nicluding the current node, but not always inclusive of all nodes in the current path (because the sum does not have to start from root) so we have to see which nodes to include.
            comboSum = sum(combo)
            targetIndex = 0
            while targetIndex < len(combo):
                if comboSum == targetSum:
                    break
                comboSum -= combo[targetIndex]
                targetIndex += 1
            result.append(combo[targetIndex:])

        seenSum[root.val + previousSum] += 1  # Keep track of prefix sum
        self.recurse(root.left, root.val + previousSum, targetSum, seenSum, combo, result)
        self.recurse(root.right, root.val + previousSum, targetSum, seenSum, combo, result)

        seenSum[root.val + previousSum] -= 1  # Backtrack back to the root so we need to erase whatever seenSum updates we did when going down the root.
        combo.pop()  # Backtrack to root so we remove the the last added node