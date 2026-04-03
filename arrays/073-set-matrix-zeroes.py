"""
73. Set Matrix Zeroes
Medium

Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Example 3:

Input: matrix = []
Output: []

Example 3:

Input: matrix = [[]]
Output: [[]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


"""


class Solution:
    # Time complexity: O(m.n), Space complexity: O(m+n)
    def setZeroes(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return matrix

        # contains rows, cols with zeroes
        zero_row, zero_col = set(), set()
        m, n = len(matrix), len(matrix[0])

        # pass 1: populate zero_row, zero_col
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)

        # pass 2: check if row/col of element is in zero_row/col
        for r in range(m):
            for c in range(n):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0
        return matrix

    # Time complexity: O(m.n), Space complexity: O(1)
    def setZeroesBetterSpace(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return matrix

        m, n = len(matrix), len(matrix[0])
        zero_in_first_row = False
        zero_in_first_col = False

        # check if first row initially contains zero
        for c in range(n):
            if matrix[0][c] == 0:
                zero_in_first_row = True
                break
        # check if first col initially contains zero
        for r in range(m):
            if matrix[r][0] == 0:
                zero_in_first_col = True
                break

        # use first row and col as markers
        # if an element in submatrix (1->m x 1->n) is zero, mark
        # corresponding row and column in first row, col as 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0

        # update submatrix with first row, col markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # if first row/col had a zero initially, set all elements
        # in row/col to zero
        if zero_in_first_row:
            for c in range(n):
                matrix[0][c] = 0
        if zero_in_first_col:
            for r in range(m):
                matrix[r][0] = 0

        return matrix
