class Node:
        def __init__(self, key=0, val=0, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])
            self.insert(self.nodeMap[key])
            return self.nodeMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])
        self.nodeMap[key] = Node(key, value)
        self.insert(self.nodeMap[key])

        if len(self.nodeMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.nodeMap[lru.key]

