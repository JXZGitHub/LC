class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        Time: O(N)
        Space: Stack: O(log(N) on balanced tree). Heap: O(N)
        """
        res = []
        self.postOrderTraversal(root, collections.defaultdict(int), res)
        return res

    def postOrderTraversal(self, root, seen, res):
        # This is post order because we don't know the full serialization of a given onde until its left and right trees are done.
        if not root:
            return '#'
        # This is a pre-order serialization (you can also do post-order, but never in-order as it can give same version for diff trees.)
        serial = str(root.val) + ',' + self.postOrderTraversal(root.left, seen, res) + ',' + self.postOrderTraversal(
            root.right, seen, res)
        if seen[serial] == 1:  # Avoid adding equivalent nodes for mulitiple same subtrees
            res.append(root)
        seen[serial] += 1
        return serial

import collections
class Solution_brute_force:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        q = collections.deque()
        if not root:
            return []
        res = set()
        seen = collections.defaultdict(list)
        q.append(root)
        while q:
            node = q.popleft()
            if node.val in seen:
                for tree in seen[node.val]:
                    if self.isSame(node, tree):
                        res.add(tree)
                        break
                else:
                    seen[node.val].append(node)
            else:
                seen[node.val].append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return list(res)

    def isSame(self, t1, t2):
        if not t1 and not t2:
            return True
        if bool(t1) ^ bool(t2):
            return False
        if t1.val != t2.val:
            return False
        return self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)





