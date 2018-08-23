# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        3-pointer solution:
        Do a preorder traversal, and keep valiating bst (prev node must be less than current node),
        as soon as it violates BST, save the prev node and current node as the swapped pair candidates.
        The 'second' memebr in that pair can change as we further go down BST because a swapped pair can result
        in multiple violations of BST, and the last violation determines the true 'second membmer' to be swapped.

        Time: O(N)
        Space: O(log(n))
        """
        self.inorderTraversal_and_swap(root)

    def inorderTraversal_and_swap(self, root):
        first, second, prev = None, None, None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if prev and prev.val >= root.val:
                    # An anomality is detected (just like in validate BST), determine the 2 potential swapped nodes:
                    if not first:
                        first = prev
                    second = root
                    # It's possible a 2nd anomality will be deteced due to a swapped pair, then update what the 2nd bad node really is.
                prev = root
                root = root.right
        if first and second:
            first.val, second.val = second.val, first.val


class Solution_straightforward:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        Straightforward solution:

        Updates the values of each node, instead of changing the node's left or right pointers.

        Perform an inorder traversal (left, root, right), and store the node and values in separate lists.
        the values will NOT be in ascending order due to 2 swapped nodes.

        Then, sort the values, and assign each value to each node in ascending order.

        Time: O(N)
        Space: O(N)
        """
        nodes, values = [], []
        self.inorderTraversal(nodes, values, root)
        values.sort()
        for i, v in enumerate(values):
            nodes[i].val = v

    def inorderTraversal(self, nodes, values, root):
        if not root:
            return
        self.inorderTraversal(nodes, values, root.left)
        values.append(root.val)
        nodes.append(root)
        self.inorderTraversal(nodes, values, root.right)