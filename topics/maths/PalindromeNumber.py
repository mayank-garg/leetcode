"""
URL: https://leetcode.com/problems/palindrome-number/
Companies:
	Amazon,3 | Google,3 | Bloomberg,2 | Apple,2 | Oracle,2

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 9:
            return True
        old = x
        new = 0
        while x:
            rem = x%10
            new = new*10 + rem
            x = x//10
        if new-old == 0:
            return True
        return False