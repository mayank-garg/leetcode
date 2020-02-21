"""
URL: https://leetcode.com/problems/daily-temperatures/
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
from collections import deque
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = deque([])
        stack = []
        while len(T) > 0:
            temp = T.pop()
            if not stack:
                result.appendleft(0)
            else:
                max_temp, pos = stack.pop()
                while max_temp <= temp and len(stack) > 0:
                    max_temp, pos = stack.pop()
                if max_temp > temp:
                    stack.append([max_temp, pos])
                    result.appendleft(pos-len(T))
                else:
                    result.appendleft(0)
            stack.append([temp, len(T)])
        return result