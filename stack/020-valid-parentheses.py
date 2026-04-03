"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:
Input: s = "())"
Output: false

Example 5:
Input: s = "()["
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            # opening bracket: add to stack
            if c in brackets_map:
                stack.append(c)

            # closing bracket: check if stack is empty or
            #   whether closing bracket matches opening one
            else:
                if not stack or brackets_map[stack.pop()] != c:
                    return False
        return not stack

