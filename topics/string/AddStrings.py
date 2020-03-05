"""
URL: https://leetcode.com/problems/add-strings/
Companies:
	Facebook,30 | Oracle,8 | Amazon,4 | Microsoft,2 | Snapchat,2
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        big, small = num1, num2
        if len(num1) < len(num2):
            small, big = num1, num2
        small = (len(big)-len(small))*"0"+small
        result = []
        for i in range(len(big)-1, -1, -1):
            a = int(big[i])
            b = int(small[i])
            _sum = carry+a+b
            carry = _sum//10
            _sum = _sum%10
            result.append(str(_sum))
        if carry:
            result.append(str(carry))
        result = result[::-1]
        return ''.join(result)