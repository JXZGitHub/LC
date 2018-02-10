from collections import defaultdict
class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msgToTime = {}
        self.msgToCount = defaultdict(int)

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
        self.msgToTime[message] = timestamp

        if lastTimeStamp is None or timestamp - lastTimeStamp > 60:
            self.msgToCount[message] = 1
        else:
            self.msgToCount[message] +=1

        if self.msgToCount[message] <= 3:
            return True
        else:
            return False
logger = Logger()

print (logger.shouldPrintMessage(1, 'a'))
print (logger.shouldPrintMessage(2, 'a'))
print (logger.shouldPrintMessage(55, 'a'))
print (logger.shouldPrintMessage(56, 'a'))
print (logger.shouldPrintMessage(56, 'a'))
print (logger.shouldPrintMessage(56, 'a'))
print (logger.shouldPrintMessage(56, 'a'))
print (logger.shouldPrintMessage(65, 'a'))
print (logger.shouldPrintMessage(65, 'b'))
print (logger.shouldPrintMessage(65, 'b'))
print (logger.shouldPrintMessage(65, 'b'))
print (logger.shouldPrintMessage(124, 'b'))
print (logger.shouldPrintMessage(200, 'a'))
print (logger.shouldPrintMessage(201, 'a'))
print (logger.shouldPrintMessage(203, 'a'))
