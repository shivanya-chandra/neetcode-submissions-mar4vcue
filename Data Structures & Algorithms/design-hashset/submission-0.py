class MyHashSet:

    def __init__(self):
        self.se = set()
        

    def add(self, key: int) -> None:
        self.se.add(key)
        

    def remove(self, key: int) -> None:
        self.se.discard(key)
        

    def contains(self, key: int) -> bool:
        if key in self.se:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)