# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        """
        Similar Solution to 'Copy Linked List with Random Pointer':
        Use BFS (queue) to reach every neighbor starting from node, then use a dictionary to store key as the original node, value as a cloned node. Then, for every neighbor of the each node off the queue, populate the v (which is the cloned node)'s neighbors with WHATEVER cloned node that each neighbor's points to according to the dict.

        When each neihgbor of node is traversed, skip any that has already been placed in the dictionary to avoid cycles.

        Time: O(V+E), V is #number of nodes, e is number of edges:
        Space: O(V)

        """
        q = deque()
        origToCopy = {}
        head = None

        # Append initial node into queue and set the head to its value.
        if node:
            q.append(node)
            origToCopy[node] = UndirectedGraphNode(node.label)
            head = origToCopy[node]

        while q:
            orig = q.popleft()  # This popped of node must have already been created in dict.
            for nb in orig.neighbors:
                if nb not in origToCopy:  # Avoid cycle, as you can have a node's neighbor that's seen before(already is a key in the dict)
                    origToCopy[nb] = UndirectedGraphNode(nb.label)  # If the original's neighbor is not in dict, create it as k,v pair.
                    q.append(nb)  # And also continue the BFS by appending the neighbor node to the queue

                origToCopy[orig].neighbors.append(origToCopy[nb])  # Now the original's neighbor must exist in dict's values, so append it to the current cloned node's neighbor.

        return head