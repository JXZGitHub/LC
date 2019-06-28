import collections


class FreqStack(object):

    def __init__(self):
        self.freq_stacks = []  # Bucket sort technique: A list of stacks whose index is the frequency of the elements in the stack, and value is a stack that contains all elements of that frequency.
        self.element_to_freq = collections.defaultdict(int)  # global mapping of element to its frequency

    def push(self, x):
        """
        :type x: int
        :rtype: None

        Time: O(1)
        Space: O(1)
        """
        self.element_to_freq[x] += 1
        freq = self.element_to_freq[x]
        if freq > len(self.freq_stacks):
            # Add a new stack to represent this new (higher) frequency.
            stack = [x]  # this new stack will hold the value with this frequency for now.
            self.freq_stacks.append(stack[:])
        else:
            stack = self.freq_stacks[freq - 1]
            stack.append(x)

    def pop(self):
        """
        :rtype: int

        Time: O(1)
        Space: O(1)

        """
        stack = self.freq_stacks[-1]
        to_return = stack.pop()  # Return the top of the stack of the most frequent element(s)
        if not stack:  # If that was the last element in this 'most frequent' stack, get rid of this stack.
            self.freq_stacks.pop()
        self.element_to_freq[to_return] -= 1  # Update global frequency mapping
        return to_return


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
print (obj.pop())
print (obj.pop())
print (obj.pop())
print (obj.pop())
