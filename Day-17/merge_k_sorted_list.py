# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        if lists==[] or lists==[[]]:
            return None
        else:
            for i in lists:
                h=i
                while h:
                    l.append(h.val)
                    h=h.next
            l.sort()
            head=None
            for i in l:
                if head is None:
                    head=ListNode(i)
                    t=head
                else:
                    a=ListNode(i)
                    t.next=a
                    t=t.next
        return head
        