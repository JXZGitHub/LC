from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteBinaryTree(self, root):
        #BST, and check every node for certain conditions.
        q = deque()
        if not root:
            return True
        q.append(root)
        should_be_last = False
        while q:
            currNode = q.popleft()

            if currNode.left:
                if should_be_last:
                    return False
                q.append(currNode.left)
            else:
                should_be_last = True

            if currNode.right:
                if should_be_last:
                    return False
                q.append(currNode.right)
            else:
                should_be_last = True
        return True

    def flushoutTree(self, q):
        while q:
            node = q.popleft()
            print (node.val)

    def printIncompleteLevel(self, root):
        #BST, and check every node for certain conditions.
        q = deque()
        if not root:
            return True
        q.append(root)
        should_be_last = False
        while q:
            currNode = q.popleft()
            if not currNode.left and not currNode.right and should_be_last:
                self.flushoutTree(q)
                break

            if currNode.left:
                q.append(currNode.left)
                #if should_be_last:
            else:
                should_be_last = True

            if currNode.right:
                #if should_be_last:
                #    self.flushoutTree(q)
                #    break
                q.append(currNode.right)
            else:
                should_be_last = True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = TreeNode(3)
root.left.left.right = TreeNode(9)
#root.right.right.left = TreeNode(8)
# root.right.right.right = TreeNode(9)
sol = Solution()
if (sol.isCompleteBinaryTree(root)):
    print ("Complete Binary Tree")
else:
    print ("NOT Complete Binary Tree")
    sol.printIncompleteLevel(root)



