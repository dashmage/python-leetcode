"""
74. Search a 2D Matrix
Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Example 3:
Input: matrix = [[1], [3], [5]], target = 3
Output: true

Example 4:
Input: matrix = [[1], [3], [5]], target = 4
Output: false
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


"""

def bin_search(nums: list[int], target: int) -> int:
    """Returns either index where target is found or the index of the element right before."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

class Solution:
    # Time complexity: O(m * logn)
    # since we're going through all the matrix[r][0] elements to create the first_elements list
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        first_elements = [matrix[r][0] for r in range(len(matrix))]
        row_idx = bin_search(first_elements, target)
        col_idx = bin_search(matrix[row_idx], target)
        return  matrix[row_idx][col_idx] == target

    # Neetcode solution: O(log(m*n))
    def searchMatrixEfficient(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # find the right row using binary search
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            # target greater than last elem in row
            if target > matrix[row][-1]:
                top = row + 1
            # target lesser than first elem in row
            elif target < matrix[row]:
                bot = row - 1
            else: # found the right row
                break

        if not (top <= bot):
            return False

        # find whether target exists in that row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        return False
