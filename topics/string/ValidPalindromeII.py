"""
URL: 
Companies:
	Facebook,51 | Microsoft,3

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def find_palindrome(s, start, end, deleted):
            while start < end:
                a, b = s[start], s[end]
                if a != b:
                    if deleted == 1:
                        return False
                    return find_palindrome(s, start+1, end, 1) or find_palindrome(s, start, end-1, 1)
                start += 1
                end -= 1
            return True
        return find_palindrome(s, 0, len(s)-1, 0)