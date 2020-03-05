"""
URL: https://leetcode.com/problems/verifying-an-alien-dictionary/
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _map = {}
        for pos, c in enumerate(order):
            _map[c] = pos
        if not words or len(words) == 1:
            return True
        min_len = len(words[0])
        max_len = len(words[0])
        consider_map = {}
        for pos, word in enumerate(words):
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))
            consider_map[pos] = True
            
        for i in range(max_len):
            for j in range(len(words)):
                if consider_map[j] and i < len(words[j]):
                    val = _map.get(words[j][i])
                    if j > 0 and i < len(words[j-1]):
                        pre_val = _map.get(words[j-1][i])
                        if val > pre_val:
                            consider_map[j] = False
                        elif val < pre_val:
                            return False
        left = 0
        for pos in consider_map:
            if consider_map[pos]:
                left += 1
        if left == 1:
            return True
        for pos, word in enumerate(words):
            if pos > 0:
                if len(word) < len(words[pos-1]):
                    return False
        return True