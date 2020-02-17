"""
URL: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
        	return ""
        pos = 0
        while True:
        	char = None
        	for _str in strs:
        		if len(_str) <= pos:
        			return _str[:pos]
        		if char is None:
        			char = _str[pos]
        		if _str[pos] != char:
        			return _str[:pos]
        	pos += 1
        return strs[0][:pos]

