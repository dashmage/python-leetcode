"""
907. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Example 4:
Input: piles = [3,6,7,11], h = 7
Output: 6

Example 5:
Input: piles = [3,6,7,11], h = 5
Output: 7

Example 6:
Input: piles = [312884470], h = 312884469
Output: 2

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109


"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        # min bananas per hour
        min_bph = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours > h:
                left = k + 1
            else:
                min_bph = min(min_bph, k)
                right = k - 1
        return min_bph
