"""
URL: https://leetcode.com/problems/design-hashmap/
Companies:
	Amazon,10 | Oracle,5 | Goldman Sachs,4 | Adobe,4 | Microsoft,3
	Google,3 | LinkedIn,2 | Tableau,2 | Dell,2 | Atlassian,2

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

"""
class Node:
    def __init__(self,key, val):
        self.val = val
        self.key = key
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr_size = 2069
        self.arr = [-1]*self.arr_size

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        _hash = key%self.arr_size
        if self.arr[_hash] == -1:
            node = Node(key, val)
            self.arr[_hash] = node
        else:
            node = self.arr[_hash]
            while node.next:
                if node.key == key:
                    node.val = val
                    return
                else:
                    node = node.next
            if node.key == key:
                    node.val = val
            else:
                node.next = Node(key, val)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        _hash = key%self.arr_size
        if self.arr[_hash] == -1:
            return -1
        node = self.arr[_hash]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        _hash = key%self.arr_size
        if self.arr[_hash] == -1:
            return
        node = self.arr[_hash]
        if node.key == key:
            self.arr[_hash] = node.next
            if not self.arr[_hash]:
                self.arr[_hash] = -1
            return
        prev = node
        node = node.next
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)