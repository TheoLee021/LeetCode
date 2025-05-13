class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.val = value
        self.next = next

class MyHashMap(object):
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)