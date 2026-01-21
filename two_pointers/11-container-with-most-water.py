"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [8,7,2,1]
Output: 7

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""


class Solution:
    # O(n) time complexity
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            cur_water = min(height[left], height[right]) * (right - left)
            max_water = max(cur_water, max_water)
            # move the pointer that points to the lower line
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

            # in case both lines are equal, moving either line inward results
            # in a container with lower capacity. This is because even if we
            # move to a taller line, the other pointer will restrict the capacity
            else:
                left += 1
                right -= 1
        return max_water
