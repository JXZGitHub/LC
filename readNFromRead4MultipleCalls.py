# # The read4 API is already defined for you.
# # @param buf, a list of characters
# # @return an integer
# # def read4(buf):

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    buffer = [None] * 4  # This buffer is persisted call to call
    locationInBuffer = 0  # The location in the current read4 buffer (ie, number of bytes that has been flushed)
    read4CharsRead = 0  # Number of chars read each time read4() is called.

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        for i in range(n):
            if self.locationInBuffer == self.read4CharsRead:
                self.read4CharsRead = read4(self.buffer)
                self.locationInBuffer = 0
                if not self.read4CharsRead:
                    return i
            buf[i] = self.buffer[self.locationInBuffer]
            self.locationInBuffer += 1
        return n


class Solution2(object):
    def __init__(self):
        self.read4Buffer = [''] * 4
        self.read4BufferLocation = 0  # Location of the buffer as returned by read4, persisted from call to call.
        self.read4CharsRead = 0  # Number of chars read by read4, persisted from call to call.

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)

        Time: O(N)
        Space: O(1)

        Difference from the single call version:
        Each time read() is called, it reads the input(not shown) starting at the file pointer from the previous call
        to read4().
        Therefore, if read() is called with N<4, and then called again, the buffer as returned from last read4() may
        have unprocessed chars that we have to flush out FIRST, before calling read4 again
        """
        currentLocationOfBuffer = 0  # Global location of the current buffer (buf) of read()
        while currentLocationOfBuffer < n:
            # This IF condition will be true on the any call to read() if the previous call's n is <4.
            # Therefore, it'll flush out whatver is unread in the read4Buffer from the previous call and store it
            # into the return buffer (buf), BEFORE keeping calling read4()
            if self.read4BufferLocation < self.read4CharsRead:
                buf[currentLocationOfBuffer] = self.read4Buffer[self.read4BufferLocation]
                currentLocationOfBuffer += 1
                self.read4BufferLocation += 1
            else:
                self.read4CharsRead = read4(self.read4Buffer)
                self.read4BufferLocation = 0
                if not self.read4CharsRead:
                    break
        return currentLocationOfBuffer
