"""
URL: https://leetcode.com/problems/string-compression/
Companies:
	Microsoft,7 | Goldman Sachs,6 | Expedia,4 | Amazon,2 | Google,2 | Apple,2 | Zillow,2

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        curr, pos = 0, 0
        count = 0
        prev = chars[curr]
        while pos < len(chars):
            if count == 0:
                chars[curr] = chars[pos]
                curr += 1
            if chars[pos] == prev:
                count += 1
            else:
                prev = chars[pos]
                if count > 9:
                    value = count
                    power = 0
                    while value//(10**power) > 0:
                        # value = value//(10^power)
                        power+=1
                    power -= 1
                    while power >= 0:
                        div = count//(10**power)
                        count = count%(10**power)
                        if div:
                            chars[curr] = str(div)
                        else:
                            chars[curr] = str(count)
                            count = 0
                        curr += 1
                        power -= 1
                elif count > 1:
                    chars[curr] = str(count)
                    curr += 1
                count = 0
                pos -= 1
            pos += 1
        if count == 0:
            chars[curr] = prev
            curr += 1
        else:
            # print(count)
            if count > 9:
                value = count
                power = 0
                while value//(10**power) > 0:
                    power+=1
                power -= 1
                while power >= 0:
                    div = count//(10**power)
                    count = count%(10**power)
                    # print(div, count)
                    if div:
                        chars[curr] = str(div)
                    else:
                        chars[curr] = str(count)
                        count = 0
                    curr += 1
                    power -= 1
            elif count > 1:
                chars[curr] = str(count)
                curr += 1
            # else:
                # curr += 1
        return curr