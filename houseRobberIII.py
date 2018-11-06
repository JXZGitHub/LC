# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time :O(N)
        Space: O(N) on stack (single list with one child all the way). O(N) on heap, which maintains the cache.

        Recursive: At each node, its maximum profit is max of (profit if we rob this node, profit if we don't rob this node)
        Robbing this node - profit is node value + all of its skip level children's max profit.
        Not Robbing - profit is its direct children's max profit.
        """
        return self.maxProfitAt(root, {})

    def maxProfitAt(self, node, cache):
        if not node:
            return 0
        if node in cache:
            return cache[node]
        # IF robbing this node, then total profit is this node and its skip level nodes.
        profit_if_robbing_node = node.val
        if node.left:
            profit_if_robbing_node += self.maxProfitAt(node.left.left, cache) + self.maxProfitAt(node.left.right, cache)
        if node.right:
            profit_if_robbing_node += self.maxProfitAt(node.right.left, cache) + self.maxProfitAt(node.right.right,
                                                                                                  cache)

        # IF NOT robbing this node, then total profit is this node's left and right children.
        profit_if_not_robbing_node = self.maxProfitAt(node.left, cache) + self.maxProfitAt(node.right, cache)

        max_profit_at_node = max(profit_if_robbing_node, profit_if_not_robbing_node)

        # Cache max profit at a visited node, so when we do node.left or node.right, we don't recompute
        cache[node] = max_profit_at_node

        return max_profit_at_node


class Solution2:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time :O(N)
        Space: O(N) on stack. O(1) on heap.

        Recursive: At each node, maintain a res list, where res[0] is max profit of robbing the node, and res[1] is max profit of not robbing.

        """
        res = self.maxProfitAt(root)
        return max(res[0], res[1])

    def maxProfitAt(self, node):
        if not node:
            return [0, 0]

        left = self.maxProfitAt(node.left)
        right = self.maxProfitAt(node.right)

        res = []
        # If robbing this node
        res.append(node.val + left[1] + right[1])
        # If not robbing this node
        res.append(max(left[0], left[1]) + max(right[0], right[1]))
        return res


