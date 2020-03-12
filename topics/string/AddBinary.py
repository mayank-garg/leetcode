"""
URL: https://leetcode.com/problems/add-binary/
Companies:
	Facebook,57 | Google,3 | Amazon,3

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        big, small = a,b
        if len(a)< len(b):
            big, small = b,a
        small = (len(big)-len(small))*"0"+small
        result = []
        carry = 0
        for i in range(len(big)-1, -1, -1):
            val1, val2 = int(big[i]), int(small[i])
            _sum = val1+val2+carry
            if _sum > 1:
                carry = 1
            else:
                carry = 0
            if _sum %2 == 0:
                _sum = 0
            else:
                _sum = 1
            result.append(str(_sum))
        if carry:
            result.append(str(carry))
        result = result[::-1]
        return "".join(result)