from collections import deque
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        Time: O(N), N is number of nodes in tree
        Space: O(H), H is height of tree
        """
        treeString = []
        self.convertToStr(root, treeString)
        return ''.join(treeString)

    def convertToStr(self, node, treeString):
        if not node:
            treeString.append('X')
            treeString.append(',')
        else:
            treeString.append(str(node.val))
            treeString.append(',')
            self.convertToStr(node.left, treeString)
            self.convertToStr(node.right, treeString)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Time: O(N), N is size of string
        Space: O(H), H is height of tree

        """
        vals = deque(data.split(','))
        return self.convertToTree(vals)

    def convertToTree(self, vals):
        if not vals:
            return None
        val = vals.popleft()
        if val != 'X':
            root = TreeNode(val)
            root.left = self.convertToTree(vals)
            root.right = self.convertToTree(vals)
            return root
        else:
            return None

col = Codec()
t = col.deserialize('1,2,4,X,X,5,X,X,3,X,X')
s = col.serialize(t)
print (t.val, t.left.val, t.right.val)
print (s)