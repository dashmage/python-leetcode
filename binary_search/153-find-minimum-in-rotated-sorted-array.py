"""
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
 
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Example 4:

Input: nums = [3,1,2]
Output: 1

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.


"""

# Rare case where the Neetcode solution seems needlessly complicated
# The aim is to find the "inflection point" where the rotation occurs
# Eg: In [3,4,5,1,2], the point is at [5, 1] and that's where we can find the min value
# It helps to work it out with a small input like [2,1] and [1,2]
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if value on right end is less than mid
            # then the inflection point has to be on the right side
            # nums[mid] can't be min value since nums[right] is already less than it
            if nums[right] < nums[mid]:
                left = mid + 1
            # keeps increasing towards the right, min has to be on the left
            # we set right to mid since mid itself could be the min value
            else:
                right = mid
        return nums[left]

