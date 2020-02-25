"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

# Approach - Recursion with memoization

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        def find_pair(pos, total, memo):
            if pos == len(nums):
                if total == S:
                    return 1
                return 0
            if (pos, total) in memo:
                return memo[(pos, total)]
            positive = find_pair(pos+1, total-nums[pos], memo)
            negative = find_pair(pos+1, total+nums[pos], memo)
            memo[(pos, total)] = positive+negative
            return memo[(pos, total)]
        result = find_pair(0, 0, memo)
        return result