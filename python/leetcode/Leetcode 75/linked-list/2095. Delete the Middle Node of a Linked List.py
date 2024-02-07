# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Delete the middle node using a fast and slow pointer.
        The middle is floor(n/2) where n is the number of nodes,
        so we choose the right middle for even sized linked list.
        """

        # Create a dummy node to handle both odd and even sized linked list
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Check for length one or zero linked list
        if not fast.next.next:
            return None

        # Move the fast pointer twice as fast as the slow pointer
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Replace middle
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    s = Solution()
    # [1,3,4,7,1,2,6]
    head = ListNode(
        1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6))))))
    )

    s.deleteMiddle(head)
    while head:
        print(head.val)
        head = head.next
