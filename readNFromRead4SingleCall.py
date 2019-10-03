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


class Solution_2(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total_read_so_far = 0
        read4Buf = [None] * 4
        while (total_read_so_far < n):
            read4_read = read4(read4Buf)
            need_to_read = min(read4_read, n - total_read_so_far)

            for i in range(need_to_read):
                buf[total_read_so_far] = read4Buf[i]
                total_read_so_far += 1
            if read4_read < 4:
                break  # No more chars remaining, so don't bother continuing even if we haven't read N chars
        return total_read_so_far