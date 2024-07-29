# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1= ListNode(0)
        d2 = ListNode(0)
        pre1 = d1
        pre2 = d2
        while head:
            if head.val <x:
                pre1.next = head
                pre1 = head
            else:
                pre2.next = head
                pre2 = head
            head= head.next
        pre2.next = None
        pre1.next = d2.next
        return d1.next
        