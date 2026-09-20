class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        dummy = ListNode()
        head = dummy

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                dummy.next = pointer1
                pointer1 = pointer1.next
            else:
                dummy.next = pointer2
                pointer2 = pointer2.next
            
            dummy = dummy.next

        dummy.next = pointer1 or pointer2

        return head.next