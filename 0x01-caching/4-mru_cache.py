#!/usr/bin/python3
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.usage_order = []  # Track the usage order of keys

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Key already exists, move it to the front of the usage order (MRU)
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Cache is full, discard the MRU item
            mru_key = self.usage_order.pop(0)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}\n")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the front of the usage order (MRU)
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
