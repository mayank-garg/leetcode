"""
URL: https://leetcode.com/problems/subtree-of-another-tree/
Companies:
	Amazon,77 | Microsoft,5 | Google,2

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def match(s, t):
            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            if s.val != t.val:
                return False
            if s.left or t.left:
                found_match = match(s.left, t.left)
            else:
                found_match = True
            if found_match and (s.right or t.right):
                found_match = match(s.right, t.right)
            return found_match
        
        def find(s, t, nodes):
            if not s:
                return None
            if s.val== t.val:
                nodes.append(s)
            if s.left:
                find(s.left, t, nodes)
            if s.right:
                find(s.right, t, nodes)
        nodes = []
        find(s, t, nodes)
        for node in nodes:
            found = match(node, t)
            if found:
                return True
        return False