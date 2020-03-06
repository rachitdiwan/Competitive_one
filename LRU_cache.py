class Node():
    def __init__(self, key = None):
        self.key = key 
        self.next = None
        self.prev = None


class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key):
        if self.head is None:
            self.head = Node(key)
            self.tail = self.head
            return
        temp = Node(key)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def remove(self): 
        if self.tail is None:
            return 
        val = self.tail.key
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def replace(self, key):
        if key == self.head.key:
            return
        temp = self.head.next
        follower = self.head
        while temp:
            if temp.key == key:
                if temp.next:
                    leader = temp.next
                    follower.next = leader
                    leader.prev = follower
                else:
                    self.tail = follower
                    follower.next = None 
                temp.next = self.head
                self.head.prev = temp
                temp.prev = None
                self.head = temp
                return
            temp = temp.next
            follower = follower.next
        return 

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.key
            temp = temp.next

    def __repr__(self):
        return str([val for val in self])





class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.counter = 0
        self.cap = capacity
        self.linklist = DoublyLinkedList()

    def get(self, key): 
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache.get(key) is None:
            return -1
        self.mru_el(key, True)
        return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.counter == self.cap:
            del_key = self.lru_el()
            del self.cache[del_key]
            self.counter -= 1
        self.cache[key] = value
        self.counter += 1
        self.mru_el(key, False)

    def lru_el(self):
        return self.linklist.remove()

    def mru_el(self,key,state):
        if state:
            self.linklist.replace(key)
            return
        self.linklist.add(key)

our_cache = LRU_Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

#Test Case 1
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)

#Test Case 2
print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(1))     

our_cache.set(11,11)
our_cache.set(10, 10)

#Test Case 3
print(our_cache.get(11))
print(our_cache.get(4))     # returns -1 because the cache reached it's capacity and 4 was the least recently used entry"""
print(our_cache.get(3)) 
