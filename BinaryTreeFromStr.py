# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode

        Time: O(len(s))
        Space: O(len(s))
        """
        if not s:
            return None
        stack = []
        i = 0
        while i < len(s):
            start = i

            if s[i] == ')':
                stack.pop() #No longer need that node anymore, as it's done.

            elif s[i] not in ('('):
                while i + 1 < len(s) and s[i + 1] not in ('(', ')', '-'):
                    i += 1 #Accumulate all digits to form a number (includin negative)
                num = int(s[start:start + (i - start) + 1]) #Take hte accumulated strings and convert to integer
                node = TreeNode(num)
                if stack:
                    top = stack[-1]
                    if not top.left:
                        top.left = node
                    elif not top.right:
                        top.right = node
                stack.append(node)
            i += 1
        return stack[-1] #Last element does not have ) in the string, so must have been left on the stack.
sol = Solution()
#print (sol.str2tree("-4(2(3)(1))(6(5)(7))"))
print (sol.str2tree("-4(2)(3)"))