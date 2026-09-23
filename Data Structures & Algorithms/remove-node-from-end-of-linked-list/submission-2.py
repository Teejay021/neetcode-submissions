# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        gholi = []
        while head:
            gholi.append(head)
            head = head.next
        
        index = len(gholi)- n
        if index == 0:
            return gholi[0].next

        gholi[index-1].next =  gholi[index].next
        return gholi[0]