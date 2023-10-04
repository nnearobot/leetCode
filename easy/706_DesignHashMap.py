# 706. Design HashMap
# easy
# https://leetcode.com/problems/design-hashmap

class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            ind = self.keys.index(key)
            self.values[ind] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            ind = self.keys.index(key)
            return self.values[ind]
        except ValueError:
            return -1    

    def remove(self, key: int) -> None:
        try:
            ind = self.keys.index(key)
            del self.keys[ind]
            del self.values[ind]
        except ValueError:
            return
