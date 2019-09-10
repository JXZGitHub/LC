# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def read(self, buf, n):
        """
        Same solution as multiple call version.

        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buffer = [None] * 4  # This buffer is persisted call to call
        locationInBuffer = 0  # The location in the current read4 buffer (ie, number of bytes that has been flushed)
        read4CharsRead = 0  # Number of chars read each time read4() is called.

        for i in range(n):
            if locationInBuffer == read4CharsRead:
                read4CharsRead = read4(buffer)
                locationInBuffer = 0
                if not read4CharsRead:
                    return i
            buf[i] = buffer[locationInBuffer]
            locationInBuffer += 1
        return n

class Solution2(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str]) #IMPORTANT: Buf is where the whatever is read is stored.
        :type n: Maximum number of characters to read (int) #This is the number of chars we can read at one time
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        buffer = [''] * 4
        for i in range(n / 4 + 1):
            size = read4(buffer) #buffer will have whatever is read from read4(at most 4 characters for each call)
            if size:
                toRead = min(size,n-read_bytes)
                buf[read_bytes:read_bytes+toRead] = buffer[:toRead] # copy whatever is read from read4 into the readN buffer, appending each time.
                read_bytes += toRead #Keep track of the number of chars read.
            else:
                break
        return read_bytes  #eg if n = 3 and input has 4 characters, then we return 3 not 4.