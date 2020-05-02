class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.p = None
        self.n = None

class DQue:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0

        self.head.n = self.tail
        self.tail.p = self.head
    
    def remove(self, node):
        p = node.p
        n = node.n
        p.n = n
        n.p = p

        self.size -= 1
    
    def add(self, node):
        node.p = self.tail.p
        node.n = self.tail
        self.tail.p.n = node
        self.tail.p = node

        self.size += 1
    
    def remove_last(self):
        last = self.head.n
        self.remove(last)
        return last

    def __str__(self):
        return "{}".format(self.size)

class LFUCache:

    def __init__(self, capacity: int):
        self.d_f = dict()
        self.d_k = dict()
        self.capacity = capacity
        self.size = 0
        self.min_f = 0

    def refresh(self, node, freq):
        self.d_f[freq].remove(node)
        if not freq + 1 in self.d_f:
            self.d_f[freq + 1] = DQue()
        
        self.d_f[freq + 1].add(node)
        self.d_k[node.key] = [node, freq + 1]
        
        if self.d_f[freq].size == 0 and freq == self.min_f:
            self.d_f.pop(freq)
            self.min_f = freq + 1
      

    def get(self, key: int) -> int:
        if not key in self.d_k:
            print("key {} not in dict".format(key))
            return -1
       
        node, freq = self.d_k[key]
        #print("get ", node.key, node.val, freq)
        #print("before: ", key, self.d_k.keys(), self.d_f.keys())
        self.refresh(node, freq)
        #print("size ", self.size, self.d_k.keys(), self.d_f.keys(), self.min_f)
        return node.val
            

    def put(self, key: int, value: int) -> None:
        if key in self.d_k:
            node, freq = self.d_k[key]
            node.val = value
            self.refresh(node, freq)
        else:
            if self.size == self.capacity:
                node = self.d_f[self.min_f].remove_last()
                self.d_k.pop(node.key)
                self.size -= 1
            
            if self.min_f != 1:
                self.d_f[1] = DQue()
            
            node = Node(key, value)
            self.d_f[1].add(node)
            self.min_f = 1
            self.d_k[key] = [node, 1]
            self.size += 1
        #print("size ", self.size, self.d_k.keys(), self.d_f.keys())


if __name__ == "__main__":

    cache = LFUCache(2)

    print("put 1 1")
    cache.put(1, 1)
    print("put 2 2")
    cache.put(2, 2)
    print("get 1:", cache.get(1))       # 返回 1
    print()
    print("put 3 3, remove 2")
    cache.put(3, 3)           # 去除 key 2
    print("get 2:", cache.get(2))       # 返回 -1 (未找到key 2)
    print()
    print("get 3:", cache.get(3))       # 返回 3
    print()
    print("put 4 4, remove 1")
    cache.put(4, 4)           # 去除 key 1
    print("get 1:", cache.get(1))       # 返回 -1 (未找到 key 1)
    print()
    print("get 3:", cache.get(3))       # 返回 3
    print()
    print("get 4:", cache.get(4))       # 返回 4
