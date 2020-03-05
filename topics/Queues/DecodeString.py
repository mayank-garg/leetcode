"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution:
    def decodeString(self, s: str) -> str:
        def is_integer(c):
            try:
                int(c)
                return True
            except Exception as e:
                return False
        
        def decode(s, pos):
            _str = ""
            while pos < len(s):
                c = s[pos]
                if is_integer(c):
                    num = int(c)
                    t_pos = pos+1
                    while is_integer(s[t_pos]):
                        num = num*10 + int(s[t_pos])
                        pos = t_pos
                        t_pos += 1
                    new_str, pos = decode(s, pos+2)
                    _str += num*new_str
                else:
                    if c == ']':
                        return _str, pos+1
                    _str += c
                    pos+=1
            return _str, pos
        res, pos = decode(s, 0)
        return res