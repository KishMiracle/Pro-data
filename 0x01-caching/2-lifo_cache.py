#!/usr/bin/python3
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the last item (LIFO)
            removed_key = self.stack.pop()
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}\n")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
