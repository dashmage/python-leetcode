"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.
 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

 
Follow up: Could you do this in one pass?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head

    # use dummy node to avoid edge case
    def removeNthFromEndUsingDummy(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next=head)
        slow = fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
    
fourth = ListNode(4, None)
third = ListNode(3, fourth)
second = ListNode(2, third)
head = ListNode(1, second)
s = Solution()
head = s.removeNthFromEnd(head, 2)
