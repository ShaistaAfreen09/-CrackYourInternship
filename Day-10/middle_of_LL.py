# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys=head
        tem=head
        while tem and tem.next:
            sys=sys.next
            tem = tem.next.next
        return sys

    