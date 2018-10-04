# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]

        Time: O(N+K), where N is number of nodes in tree.
        Space: O(max(log(N), K)) on stack. O(N) on heap.
        """
        # DFS to create a undirected graph keep tracking of all connected nodes: parent->child and child->parent
        graph = collections.defaultdict(list)
        self.dfs(root, None, graph)
        q = [target.val]
        seen = set([target.val])

        # Perform BFS (without using a deque(),faster. But can also use a deque as traditionallly.) K number of times.
        for i in range(K):
            newQ = []
            for node in q:
                for neighbor in graph.get(node, []):
                    if neighbor not in seen:  # To avoid cyclic visits: nodeA->NodeB then nodeB->NodeA again.
                        newQ.append(neighbor)
                        seen.add(neighbor)
            q = newQ
        return q

    def dfs(self, root, parent, graph):
        if not root:
            return
        if parent:
            graph[root.val].append(parent.val)
            graph[parent.val].append(root.val)
        self.dfs(root.left, root, graph)
        self.dfs(root.right, root, graph)
