"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #issue is the random pointer that can point to another copy so can't just make new copies
        #for every single node encountered gotta see if we have the node, if yes then connect the
        #random pointer to it possible hashmap implementation 

        #was thinking start wiht the head and make a copy and have a seen hashset so if we have created
        #a copy for it we just connect it to that but how does it work acutally 
        #on the real list iterate through since we have head on each iteration add the nodes to a 
        #hashset and then whenever we enounter one in seen we will but how does that help in 
        #implementation? one thing is not clear is are we given arrays or what was thinking to store the 
        #made copies in an hashmap or something so I can handle mapping the random pointer value to 
        #a copy I have already made

        mapper = {None: None}
        pointer = head
        while pointer:
            mapper[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            mapper[pointer].next = mapper[pointer.next]
            mapper[pointer].random = mapper[pointer.random]
            pointer = pointer.next

        return mapper[head]
