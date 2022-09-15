import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Notes: 
        # 1. Both list could be different lengths
        
        # steps (iterate of list1 and list2 -> if they are not empty)
        # 1. get the values of nodes
        # 2. determine the smaller node value
        # 3. append smaller node value to new linked list
        # 4. increment smaller node value list pointer (keep the other pointer fixed)
        # 5. repeat steps 1-4
        
        # create head 
        head = ListNode()
        cur_merge = head
        
        while(list1 or list2):
            # get values of lists
            l1_val = list1.val if list1 else sys.maxsize
            l2_val = list2.val if list2 else sys.maxsize
            print(l1_val,l2_val)
            # determine smaller value
            if l1_val < l2_val:
                # create new node
                new_node = ListNode(l1_val)
                cur_merge.next = new_node
            
                # update lists pointers
                cur_merge = cur_merge.next
                list1 = list1.next if list1 else None
            else:
                 # create new node
                new_node = ListNode(l2_val)
                cur_merge.next = new_node
            
                # update lists pointers
                cur_merge = cur_merge.next
                list2 = list2.next if list2 else None
                
        return head.next
        