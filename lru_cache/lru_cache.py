from doubly_linked_list import DoublyLinkedList


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
        # self.cache = {}
        # self.storage = DoublyLinkedList()
        self.order = DoublyLinkedList()
        self.cache = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # def get(self, key):
    #     # If key already exists, move to front (most recent) and return the value
    #     if key in self.cache:
    #         node = self.cache[key]
    #         self.storage.move_to_front(node)
    #         return node.value[1]

    #     # If key doesn't exist, return None
    #     else:
    #         return None
    def get(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache[key]
            self.order.move_to_front(node)
            return node.value[1]

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

    # def set(self, key, value):
    #     # If key already exists, replace with incoming value, then move to front (most recent)
    #     if key in self.cache:
    #         node = self.cache[key]
    #         node.value = (key, value)
    #         return self.storage.move_to_front(node)

    #     # If hitting the max cache limit, delete oldest from the tail
    #     if self.storage.length == self.limit:
    #         del self.cache[self.storage.tail.value[0]]
    #         self.storage.remove_from_tail()

    #     # Otherwise, add incoming key:value pair to the head (most recent)
    #     self.storage.add_to_head((key, value))
    #     self.cache[key] = self.storage.head

    def set(self, key, value):
        # if item/key already exists
        if key in self.cache:
            # overwrite the value
            node = self.cache[key]
            # assign node value to be key:value tuple
            node.value = (key, value)
            # move to the head (most recently used)
            self.order.move_to_front(node)
            return

        # size is at the limit
        if len(self.order) == self.limit:
            # evict the oldest from tail in both the cache
            oldest_index = self.order.tail.value[0]
            del self.cache[oldest_index]
            self.order.remove_from_tail()

        # size is not at limit for adding new item, add new to the front
        self.order.add_to_head((key, value))
        self.cache[key] = self.order.head
