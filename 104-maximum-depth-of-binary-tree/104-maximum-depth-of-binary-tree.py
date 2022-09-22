# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # steps (using dfs to find longest path)
        # 1. start at the root node
        # 2. Does node have neighbors?
        #   2.1 yes 
        #       2.1.1 add neighors to stack
        #       2.1.2 goto left neighbor and increment count, remove node from stack
        #       2.1.3 repeat step2
        #   2.2 no 
        #       2.2.1 if stack empty:
        #           2.2.1.1 no - goto next node in stack
        #           2.2.1.2 yes - goto step3
        #       2.2.2 repeat step2
        
#         Recursive Method
#         depth = 0

#         def dfs(node, depth):
#             if node is not None:
#                 return max(dfs(node.left,depth+1), dfs(node.right,depth+1))
#             else:
#                 return depth
            
        
#         return dfs(root, depth)

        # Iterative Method

        # steps:.
        # 1. add root to stack
        # 2. is stack node is not none 
        #   2.1 Yes 
        #       2.1.1 Add left and right to stack
        #       2.1.2 Increment count
        #   2.2 No
        #       2.2.1 if maxcnt is less than cnt set it to cnt
        #       2.2.2 
        
#         stack = [[root,1]]
        
#         # stores max depth
#         max_dpt = 0
#         cnt = 0
#         none_cnt
#         while(len(stack) > 0):
#             # pop the value from the stack
#             print(stack)
#             node = stack.pop()
#             print(node)
            
#             if node is not None:
#                 # add neighbors to stack
#                 stack.append(node.left)
#                 stack.append(node.right)
#                 cnt+=1
#             else:
#                 if max_dpt < cnt:
#                     max_dpt = cnt
#                 cnt-=1
                
#         return max_dpt

        stack = [[root,1]]
        max_dpt = 0
        while(stack):
          
            node, depth = stack.pop()
            
            if node is not None:
                # add neighbors to stack
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1]) 
       
                if max_dpt < depth:
                    max_dpt = depth
              
        return max_dpt
            