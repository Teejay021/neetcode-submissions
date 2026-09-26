class Node:
    def __init__(self,key,val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:

    #left = LRU, right = most recent
    def __init__(self, capacity: int):
        self.cache = {} #map key to nodes
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]











