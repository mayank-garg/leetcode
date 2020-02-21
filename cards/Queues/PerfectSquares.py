"""
URL: https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import math
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def square(num):
            if cache.get(num):
                return cache[num]
            if num == 0:
                return 0
            root = int(math.sqrt(num))
            min_path = num
            for i in range(root, 1, -1):
                min_path = min(min_path, square(num-(i*i))+1)
            cache[num] = min_path
            return min_path
        val = square(n)
        return val