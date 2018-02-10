class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msgToTime = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        lastTimeStamp = self.msgToTime.get(message)
        if lastTimeStamp is None or timestamp - lastTimeStamp >= 10:
            self.msgToTime[message] = timestamp
            return True
        else:
            return False