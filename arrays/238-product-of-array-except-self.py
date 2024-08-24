"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
# Really whacky intuition needed to figure out how to do this, esp in O(1) memory
# NeetCode helps again with the very informative step-by-step reasoning
# https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_

# easier to think of the elements in the list as [a, b, c, d] and visualize how 
# you get the result as [bcd, acd, abd, abc]


class Solution:
    # O(n) time complexity, O(1) space complexity
    # modifying result list directly instead of using 2 separate lists
    # for prefix and suffix products
    def productExceptSelf_v2(self, nums: list[int]) -> list[int]:
        prefix_product, suffix_product = 1, 1
        result = []
        for i in range(len(nums)):
            result.append(prefix_product)
            prefix_product *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        return result
