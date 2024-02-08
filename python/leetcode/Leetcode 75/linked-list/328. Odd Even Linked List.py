# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sort the list into odd and even nodes, the first node is considered odd, and sort
        into odd first and then even.
        """
        if not head:
            return head

        oddSentinel = odd = ListNode(0, head)
        evenSentinel = even = ListNode(0, head.next)

        i = 1
        while head:
            if i % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
            i += 1

        odd.next = evenSentinel.next
        even.next = None

        return oddSentinel.next


if __name__ == "__main__":
    # [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    s.oddEvenList(head)
    while head:
        print(head.val)
        head = head.next
