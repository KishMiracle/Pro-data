#!/usr/bin/python3
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency_counter = {}  # Track the frequency of each key

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Key already exists, increase its frequency
            self.frequency_counter[key] += 1
        else:
            # Add new key with frequency 1
            self.frequency_counter[key] = 1

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Cache is full, discard the LFU item
            lfu_keys = [k for k, v in self.frequency_counter.items() if v == min(self.frequency_counter.values())]
            if len(lfu_keys) > 1:
                # If there are multiple LFU keys, use LRU algorithm to decide which to discard
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                self.frequency_counter.pop(lru_key)
                print(f"DISCARD: {lru_key} (LFU tiebreaker)\n")
            else:
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                self.frequency_counter.pop(lfu_key)
                print(f"DISCARD: {lfu_key} (LFU)\n")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Increase frequency and move key to correct position in usage_order
        self.frequency_counter[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
