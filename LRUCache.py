class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        """

        :rtype: object
        """
        self.head = None
        self.tail = None

    def insert(self,node):
        node.next = None
        node.prev = None
        if not self.head and not self.tail:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = None
        node.prev = None


    def __str__(self):
        currNode = self.head
        allNodes=[]
        while (currNode):
            allNodes.append([currNode.key, currNode.val])
            currNode = currNode.next
        return str(allNodes)
if __name__ == 'main':
    l = LinkedList()
    one=ListNode('a',1)
    two=ListNode('b',2)
    three=ListNode('c',3)
    four=ListNode('d',4)
    l.insert(one)
    l.insert(two)
    l.insert(three)
    l.insert(four)
    print (l)
    l.remove(three)
    print (l)
    l.insert(three)
    print (l)
# l.remove(one)
# print (l)
# l.remove(three)
# print (l)
#
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.list = LinkedList()

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.cache[key]=node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        valueNode = self.cache[key] #valueNode here is a ListNode object (key, value)
        #Deletes, and then inserts, the item into the queue(linkedlist) to the end (most recent).
        self.list.remove(valueNode)
        self._insert(key, valueNode.val)
        return valueNode.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.list.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            toBeDeleted = self.list.head #toBeDeleted is a ListNode object (key, value)
            del self.cache[toBeDeleted.key]
            self.list.remove(toBeDeleted)
        self._insert(key, value)

from Lib.collections import OrderedDict
class LRUCache2:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key] #Delete the key from ordered dict
        self.cache[key]=val #And put it back in again, so it ends up in the 'last' (most recently used) position.
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False) #Gets the 'first' (least recently used, last=False) item from OrderedDict.
        self.cache[key] = value

if __name__ == 'main':
    print ("Queue as doubly-linked list implementation")
    cache = LRUCache(3)
    cache.put(1, 'one')
    cache.put(2, 'two')
    cache.put(3, 'three')
    print (cache.get(1))
    cache.put(4, 'four')
    print (cache.get(2))
    print (cache.get(4))
    cache.put(5, 5)
    print (cache.get(4))
    print (cache.get(3))
    print ("OrderedDict implementation")
    cache = LRUCache2(3)
    cache.put(1, 'one')
    cache.put(2, 'two')
    cache.put(3, 'three')
    print (cache.get(1))
    cache.put(4, 'four')
    print (cache.get(2))
    print (cache.get(4))
    cache.put(5, 5)
    print (cache.get(4))
    print (cache.get(3))