# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create head to be able to start indexing nodes to store output
        head = ListNode()
        # pointer
        cur =  head
        
        carry = 0
        # iterate over the node to add
        while(l1 or l2 or carry!=0):
            # get values
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            # print(l1_val,l2_val)
            
            # add values
            val = l1_val + l2_val + carry
            carry =  val//10
            val = val%10
            
            # add val to linked list
            new_node = ListNode(val)
            cur.next = new_node
            cur = cur.next
            
            # update l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next