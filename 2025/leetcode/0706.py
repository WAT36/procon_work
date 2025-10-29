class MyHashMap:

    def __init__(self):
        self.m={}

    def put(self, key: int, value: int) -> None:
        self.m[key]=value

    def get(self, key: int) -> int:
        return self.m[key] if key in self.m.keys() else -1

    def remove(self, key: int) -> None:
        if key in self.m.keys():
            self.m.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)