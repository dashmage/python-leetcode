"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.
 
Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:


Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head: ListNode | None) -> ListNode | None:
        current, prev = head, None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    # head is going to the last node each recursive loop and eventually becomes the last node of the reversed list
    # head.next.next = head --> set the next node's next pointer to the current head
    # new_head (the last node of the original list) stays the head of the new list for the entire recursion
    # each time you unwind out of the recursive loop, another node is added to the end.
    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseListRecursive2(self, head):
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)
        return reverse(head, None)
