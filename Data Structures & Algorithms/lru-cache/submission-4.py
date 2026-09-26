class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.stack:
                self.stack.remove(key)

            self.stack.append(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value

            self.stack.remove(key)
            self.stack.append(key)
            return

        if len(self.cache) == self.capacity:
            recent_key = self.stack.pop(0)
            self.cache.pop(recent_key)

        self.cache[key] = value
        self.stack.append(key)