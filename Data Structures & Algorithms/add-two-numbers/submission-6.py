# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer1 = l1
        pointer2 = l2
        carryOver = 0
        dummy = ListNode()
        head = dummy

        while pointer1 and pointer2:
            sum = pointer1.val + pointer2.val + carryOver
            if sum >= 10:
                carryOver = 1
                sum -= 10
            else:
                carryOver = 0

            dummy.next = ListNode(sum)
            dummy = dummy.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        while pointer1:
            sum = pointer1.val + carryOver
            if sum >= 10:
                carryOver = 1
                sum -= 10
            else:
                carryOver = 0
            
            dummy.next = ListNode(sum)
            dummy= dummy.next
            pointer1 = pointer1.next
 
        while pointer2:
            sum = pointer2.val + carryOver
            if sum >= 10:
                carryOver = 1
                sum -= 10
            else:
                carryOver = 0
            
            dummy.next = ListNode(sum)
            dummy = dummy.next
            pointer2 = pointer2.next

        if carryOver == 1:
            dummy.next = ListNode(1)


        return head.next