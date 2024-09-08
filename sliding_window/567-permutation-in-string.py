"""
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Example 3:

Input: s1 = "adc", s2 = "dcda"
Output: true

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            s2_window_counter = Counter(s2[i : i + len(s1)])
            if s1_counter == s2_window_counter:
                return True
        # similar to
        # left, right = 0, len(s1)
        # while right <= len(s2):
        #     s2_window_counter = Counter(s2[left:right])
        #     if s1_counter == s2_window_counter:
        #         return True
        #     left += 1
        #     right += 1
        return False
