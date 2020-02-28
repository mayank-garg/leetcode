"""
URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        _map = {}
        size = len(words[0])
        words_len = len(words)
        end = len(s)-(words_len*size)
        result = []
        for i in range(end):
            _count = 0
            for word in words:
                _map[word] = _map.get(word, 0)+1
            for j in range(i, i+words_len*size, size):
                _word = s[j:j+size]
                if not _map.get(word):
                    break
                _map[word] -= 1
                if _map[word] < 0:
                    break
                elif _map[word] == 0:
                     _count +=1
            if _count == words_len:
                result.append(i)
        return result