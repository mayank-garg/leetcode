"""
URL: https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def max_heapify(arr, i, size):
            left, right = 2*i, 2*i+1
            largest = i
            if left < size and arr[left].val > arr[largest].val:
                largest = left
            if right < size and arr[right].val > arr[largest].val:
                largest = right
            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                max_heapify(arr, largest, size)
        
        def add_max_heap(arr, elem):
            arr.append(elem)
            i = len(arr)-1
            while i > 1 and arr[i//2].val < arr[i].val:
                arr[i//2], arr[i] = arr[i], arr[i//2]
                i = i//2
            # max_heapify(arr, size-1, size)
        
        def heap_sort(arr, size):
            arr_size = size
            for i in range(size-1, 1, -1):
                arr[i], arr[1] = arr[1], arr[i]
                arr_size -= 1
                max_heapify(arr, 1, arr_size)
            
        arr = [0]
        for _list in lists:
            root = _list
            while root:
                add_max_heap(arr, root)
                root = root.next
        size = len(arr)
        if size == 1:
            return None
        heap_sort(arr, size)
        head, node = arr[1], arr[1]
        for i in range(2, size):
            # print(arr[i].val)
            node.next = arr[i]
            node = node.next
        node.next = None
        return head