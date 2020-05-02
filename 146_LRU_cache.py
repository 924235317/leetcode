class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dict = dict()
        self._queue = list()

    def get(self, key: int) -> int:
        if key in self._dict:
            idx = self._dict[key]
            for k, v in self._dict.items():
                if v > idx:
                    self._dict[k] -= 1
            v = self._queue.pop(idx)
            self._dict.pop(key)
            self._queue.append(v)
            self._dict[key] = len(self._queue) - 1
            
            return self._queue[self._dict[key]]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            idx = self._dict[key]
            
            for k, v in self._dict.items():
                if v > idx:
                    self._dict[k] -= 1
            self._queue.pop(idx)
            self._dict.pop(key)
        else:
            if len(self._queue) + 1 > self._capacity:
                self._queue.pop(0)
                idx_key = None
                for k, v in self._dict.items():
                    if v > 0:
                        self._dict[k] -= 1
                    elif v == 0:
                        idx_key = k
                self._dict.pop(idx_key)
        self._queue.append(value)  
        self._dict[key] = len(self._queue) - 1
