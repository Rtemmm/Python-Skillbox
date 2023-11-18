from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    @property
    def oldest(self):
        return next(iter(self.cache))

    @oldest.setter
    def oldest(self, key_value):
        key, value = key_value
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

    def print_cache(self):
        print(', '.join(f'{k} : {v}' for k, v in self.cache.items()))


cache = LRUCache(3)
cache.oldest = ("key1", "value1")
cache.oldest = ("key2", "value2")
cache.oldest = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.oldest = ("key4", "value4")
cache.print_cache()
