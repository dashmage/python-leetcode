"""
150. Evaluate Reverse Polish Notation
Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Example 4:
Input: tokens = ["18"]
Output: 18

Example 5:
Input: tokens = ["4", "3", "-"]
Output: 1
 
Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


"""
class Solution:
    # using eval()
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = "+-*/"
        for t in tokens:
            if t in operators:
                op1, op2 = stack.pop(), stack.pop()
                # wrapped around int for division rouding to zero
                result = int(eval(f"{int(op2)}{t}{int(op1)}"))
                stack.append(result)
            else:
                stack.append(int(t))
        return stack.pop()

    # without using eval()
    def evalRPN2(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op2 - op1)
            elif t == "/":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(op2 / op1))
            else:
                stack.append(int(t))
        return stack.pop()
