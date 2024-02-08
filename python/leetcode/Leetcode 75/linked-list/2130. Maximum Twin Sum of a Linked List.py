# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """Calcualte the minimum pair sum for twin nodes,
        using a set to store the values of the nodes,
        and two pointers to traverse the list.
        """
        if not head:
            return 0

        slow = fast = Sentinel = ListNode(0, head)

        # Iterate until fast node reaches the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Create a set to store the values of the nodes
        minSum = float("inf")
        fast = Sentinel.next
        slow = slow.next

        # Iterate until slow node reaches the end of the list
        while slow:
            minSum = min(minSum, slow.val + fast.val)
            slow = slow.next
            fast = fast.next

        return minSum


if __name__ == "__main__":
    # [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s = Solution()
    s.pairSum(head)
    while head:
        print(head.val)
        head = head.next
