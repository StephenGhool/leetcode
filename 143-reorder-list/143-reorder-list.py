# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Steps:
        # 1. find the half way point of the list
        # 2. reverse the nodes after the half way point
        # 3. 
        
        # find the half way point
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # reverse the second half
        second = slow.next
        prev = slow.next = None
        
        while(second):
            nextnode = second.next if second else None
            second.next = prev
            prev = second
            second = nextnode
            
        # combine both linked list to form reordered list
        headptr = head
        while(prev):
            nxt_tail_node = prev.next
            nxt_head_node = headptr.next
            
            headptr.next = prev
            prev.next = nxt_head_node
            
            headptr = nxt_head_node
            prev = nxt_tail_node
            
     
        
# Exceeded time limit

#         # steps:
#         # 1. get two pointers -> head and tail
#         # 2. ensure that head and tail are not pointing to the same node
#         # 3. store head.next and tail.next in two temp variables
#         # 4. set head.next to tail
#         # 5. set tail.next to headtmp and 
        
#         # intialize ptr
#         tail = ListNode()
#         prevtail = head
#         headptr =  head
        
#         # edge cases
#         if(head.next is None or head.next.next is None):
#             return
        
#         while(prevtail.next or headptr.next):
#             # get tail and prevtail ptrs
#             while(prevtail.next.next is not None):
#                 prevtail = prevtail.next
#             tail = prevtail.next
            
#             if prevtail == headptr:
#                 return
            
#             # update tmp variable
#             headtmp = headptr.next
#             tailtmp = tail.next
            
#             # insert tail
#             headptr.next = tail
#             tail.next = headtmp
#             prevtail.next = tailtmp
        
#             # update headptr
#             headptr = headptr.next.next if headptr else None
#             prevtail = headptr
          