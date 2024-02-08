# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head):
        """Calculate the maximum sum of a pair of twin nodes from the linked list."""
        slow = head
        fast = head
        maxVal = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nextNode, prev = None, None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        slow
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal


if __name__ == "__main__":
    # [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    s = Solution()
    s.pairSum(head)
    while head:
        print(head.val)
        head = head.next
