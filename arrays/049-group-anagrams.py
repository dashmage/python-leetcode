"""
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Example 4:
Input: strs = ["aaab", "aab"]
Output: [["aaab"],["aab"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


"""


from collections import defaultdict

class Solution:
    # O(m*n) time complexity
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # hash map where each key is a 26-length tuple representing character frequencies,
        # and each value is a list of strings belonging to that anagram group.
        freq_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freq_map[tuple(count)].append(s)
        return list(freq_map.values())

    # O(m * nlogn) time complexity
    # where m = number of strings, n = len of longest string
    def group_anagrams_slow(self, strs: list[str]) -> list[list[str]]:
        # sorted letters mapped to all the words that can be formed from it
        anagram_map = defaultdict(list)
        for word in strs:
            anagram_map[''.join(sorted(word))].append(word)
        return list(anagram_map.values())
