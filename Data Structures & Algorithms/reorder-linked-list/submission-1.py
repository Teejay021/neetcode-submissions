# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return None
        
        stack = []

        pointer = head
        while pointer:
            stack.append(pointer)
            pointer = pointer.next

        size = len(stack)
        half_size = size/2
        pointer = head
        while size > half_size:
            if pointer is stack[-1] or pointer.next is stack[-1]:
                stack[-1].next = None
                break
            
            next_node = pointer.next
            pointer.next = stack[-1]
            stack.pop()
            pointer.next.next = next_node
            pointer = next_node
            size -= 1

        return