class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.dict = {}
        self.list = []
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict:
            for i in range(len(self.list)):
                if self.list[i] == key:
                    self.list.pop(i)
                    self.list.insert(0, key)
            return self.dict[key]
        else:
            return None 


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.dict:
            self.dict[key] = value
            for i in range(len(self.list)):
                if self.list[i] == key:
                    self.list.pop(i)
                    self.list.insert(0, key)
        elif self.length < self.limit:
            self.length += 1
            self.dict[key] = value
            self.list.insert(0, key)
        else:
            del self.dict[self.list[-1]]
            self.list.pop(-1)
            self.dict[key] = value
            self.list.insert(0, key)
