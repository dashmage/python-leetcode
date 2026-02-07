"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.


"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)pass

# Doubly Linked List is used since we want to add element at the end
class DLLNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # hashmap is used to map keys to nodes for O(1) access time
        self.hashmap: dict[int: DLLNode] = {}
        # head -> tail is LRU to MRU
        # new elements are added at the tail
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: DLLNode) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node: DLLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        """
        Fetch key from cache.

        - If key doesn't exist, return -1
        - Fetch value of key from hashmap, move it to most recently used position
        """
        if key not in self.hashmap:
            return -1
        self.remove_node(self.hashmap[key])
        self.add_to_tail(self.hashmap[key])
        return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:
        """
        Put new key into cache.

        - If key already exists, overwrite its value
        - Create new node with key: value and add it to tail (MRU position)
        - If exceeding capacity, remove the LRU key (node at head)
        """
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        node = DLLNode(key, value)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)

