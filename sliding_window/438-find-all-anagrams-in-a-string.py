"""
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.


"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        left, right = 0, 0
        result = []
        expected_freq, window_freq = [0] * 26, [0] * 26
        for c in p:
            expected_freq[ord(c) - ord('a')] += 1
        while right < len(s):
            window_freq[ord(s[right]) - ord('a')] += 1
            if right - left + 1 == len(p):
                if window_freq == expected_freq:
                    result.append(left)
                window_freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            right += 1
        return result


