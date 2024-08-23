"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

1 <= n <= 8


"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                result.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        backtrack(0, 0, "")
        return result
