# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            #current node -> next n -> n -> n->... -> n
            #need another pointer on the next one where it sets the 
            #need a dummy one for now so
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev
        