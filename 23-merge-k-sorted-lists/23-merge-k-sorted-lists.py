import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergelist(self, list1, list2):
        # create head 
        head = ListNode()
        cur_merge = head
        
        while(list1 or list2):
            # get values of lists
            l1_val = list1.val if list1 else sys.maxsize
            l2_val = list2.val if list2 else sys.maxsize
           
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
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Steps:
        # 1. select two lists to merge
        # 2. merge two lists in ascending order
        # 3. repeat steps 1 and 2 for every other pair of lists
        # 4. update lists variable to store merged lists
        # 5. repeat steps 1-4 until lists variable = 1
        # 6. return list 
        
       # edge cases
        if len(lists) == 0:
            return None
        
        while(len(lists) > 1):    
            mergedlist = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                mergedlist.append(self.mergelist(l1,l2))
              
            lists = mergedlist
            
            
        return lists[0]
        
        
        # steps: version 1
        # 1. create head of the merged sorted list
        # 2. determine value to add to new list
        #   2.1 intialize min_val variable to max (int)
        #   2.2 compare node val to minval 
        #   2.3 store node index & val in hash map (val as key)
        #   2.4 repeat steps 2.2 and 2.3 for other nodes
        #   2.5 increment the node that has the smallest val
        # 3. add value to list
        # 4. repeat steps 2-3 until end of lists
        
        # Steps: version 2 (given that there are two lists)
        # 1. create head 
        # 3. merge two linked list together (know this from previous leetcode)
        # 4. repeat by merging one by one to the previously created list
        
        # edge cases to consider
        # 1. all lists are not the same length -> shortest list finishes first
        #   1.1 could set the shortest list to max int if None?
        #   1.2 
        # 2. The terminating condition since we wil have various nodes
        #   2.1 
        
        # works but exceeds time limit
#         # dummy nodes
#         dummy1_head = ListNode(-sys.maxsize)
#         dummy2_head = ListNode(-sys.maxsize)
        
#         # dummy pointer
#         d1 =  dummy1_head
#         d2 =  dummy2_head
        
        
#         # iterate over list -> to merge 1 by 1
#         for i in range(len(lists)):
#             # select two list (to perform merging)
#             l1 = lists[i]
            
#             while(l1 or d1):
#                 l1val = l1.val if l1 else sys.maxsize
#                 d1val = d1.val if d1 else sys.maxsize
                
#                 if l1val < d1val:
#                     new_node = ListNode(l1val)
#                     d2.next = new_node
#                     l1 = l1.next if l1 else None
#                 else:
#                     new_node = ListNode(d1val)
#                     d2.next = new_node
#                     d1 = d1.next if d1 else None
                   
#                 d2 =  d2.next
                
#             # reset pointers
#             d1 = dummy2_head.next
#             dummy2_head = ListNode(-sys.maxsize)
#             d2 = dummy2_head
            
#         return d1.next


      
                    
                
