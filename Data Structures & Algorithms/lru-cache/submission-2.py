class Node:
    def __init__(self, ind=0,val=0, nex=None, prev=None):
        self.val = [ind,val]
        self.nex = nex
        self.prev = prev

class LRUCache:


    def __init__(self, capacity: int):

        self.size = capacity

        self.head = Node()
        self.tail = Node()
        self.head.nex = self.tail
        self.tail.prev = self.head

        self.mp = {}

    def get(self, key: int) -> int:
        if key in self.mp:
            val = self.mp[key].val[1]
            self.put(key, val)
            return val
        else:
            return -1
        
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.mp:
            self.mp[key].prev.nex, self.mp[key].nex.prev = self.mp[key].nex, self.mp[key].prev
        
        temp = Node(key, value, self.tail, self.tail.prev)
        self.tail.prev.nex = temp
        self.tail.prev = temp
        self.mp[key] = temp
        if len(self.mp) > self.size:
            valu = self.head.nex.val[0]
            self.mp.pop(valu, None)
            self.head.nex, self.head.nex.prev = self.head.nex.nex, self.head