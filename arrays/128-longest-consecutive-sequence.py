"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,2,0,1]
Output: 3

Example 4:
Input: nums = [0]
Output: 1

Example 4:
Input: nums = []
Output: 0
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


"""


class Solution:
    # O(n) time and space complexity
    def longestConsecutive(self, nums: list[int]) -> int:
        all = set(nums)
        maxlen = 0
        for n in nums:
            # check if element is the start of a sequence
            # meaning the number before the element doesn't exist in the set
            if n - 1 not in all:
                seqlen = 1
                # count number of elements in the sequence
                while n + seqlen in all:
                    seqlen += 1
                maxlen = max(maxlen, seqlen)
        return maxlen

