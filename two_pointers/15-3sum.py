"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = []
        nums.sort()
        for i in range(len(nums)):
            # triplets consisting of postive nums will never sum to 0
            if nums[i] > 0:
                break
            # Avoid duplicate triplets, skip 'a' if it's the same as previous num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Find all pairs that sum to a target of '-a' (-nums[i])
            pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]] + pair)
        return triplets


def pair_sum_sorted_all_pairs(
    nums: list[int], start: int, target: int
) -> list[list[int]]:
    pairs = []
    left, right = start, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # Avoid duplicate [b, c] pairs, skip 'b' if it's the
            # same as prev number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs


def validate(actual, expected):
    from collections import Counter

    actual_converted = set(str(x) for x in (Counter(triplet) for triplet in actual))
    expected_converted = set(str(x) for x in (Counter(triplet) for triplet in expected))
    return actual_converted == expected_converted
