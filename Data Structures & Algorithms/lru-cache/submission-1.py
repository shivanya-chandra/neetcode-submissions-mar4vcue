class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.dummyLeft = Node(0, 0)   # LRU side
        self.dummyRight = Node(0, 0)  # MRU side

        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node):
        prev = self.dummyRight.prev
        nxt = self.dummyRight

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            lru = self.dummyLeft.next
            self.remove(lru)
            del self.cache[lru.key]