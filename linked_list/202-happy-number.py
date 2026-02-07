"""
202. Happy Number
Easy

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1


"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = get_next_num(slow)
            fast = get_next_num(get_next_num(fast))
            if fast == 1:
                return True
            # floyd's cycle detection algorithm
            # if fast and slow pointers meet, a cycle is detected
            # hence, n is not a happy number
            elif fast == slow:
                return False

def get_next_num(n: int) -> int:
    next_num = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        next_num += digit * digit
    return next_num

