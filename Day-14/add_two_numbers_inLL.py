# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        current = head

        result = l1.val + l2.val
        carry = result // 10
        current.val = str(result)[-1]

        l1 = l1.next
        l2 = l2.next

        while l1 or l2 :
            new = ListNode()
            current.next = new
            current = new

            result = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = result // 10
            current.val = str(result)[-1]
 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            new = ListNode()
            new.val = carry
            current.next = new

        return head

        