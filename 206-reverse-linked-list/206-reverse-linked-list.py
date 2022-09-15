# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Steps (iterative)
        # 1. check if node.next is None -> return None
        # 2. Set reversednode to head node and increment head cur -> set reversednode to point to null
        # 3. set prevnode.next tp None
        # 4. set curnode.next to prevnode
        # 4. increment curnode and prevnode
        
        # steps (recursive)
        # 1. next node until next is None return presentnode.next
        
        # edge cases
        if head is None:
            return head
    
        # initalize
        prevnode = head if head else None
        curnode = head.next if head else None
        # set prev node to null
        prevnode.next = None
        
        while(curnode):
            nextnode = curnode.next if curnode else None
            curnode.next = prevnode
            
            # increment pointers
            prevnode = curnode
            curnode = nextnode
        
        return prevnode
            