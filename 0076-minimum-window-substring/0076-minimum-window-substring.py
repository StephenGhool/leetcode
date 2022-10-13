class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # steps
        # 1. intialize two pointers at s
        # 2. check if right pointer char in t
        #   2.1 yes it is in t
        #       2.1.1 increment right pointer
        #       2.1.2 increment counter
        #   2.2 no
        #       2.2.1 count is non zero 
        #           2.2.1.1 increment Right ptr
        #       2.2.2 count is zero
        #           2.2.2.1 increment R&L ptrs
        # 3. is all chars within R & L (count==len(t))
        #   3.1 yes
        #       3.1.1 output length is > R-L 
        #           3.1.1.1 set output to char in L->R
        #           3.1.1.2 set left pointer R and count to zero
        #       3.1.2 output length is < R-L 
        #           3.1.2.1 do not change output
        #   3.2 no
        #       3.2.1 repeat from step1
        
        # edge cases
        if len(t) > len(s): return ""
        if s==t: return s
      
        
#         for ptr2 in range(len(s)):
#             if s[ptr2] in t_list:
#                 count+=1
#             elif count==0:
#                 ptr1+=1
      
#             if count==len(t) and (len(output) >= (ptr2-ptr1+1)):
#                 output = s[ptr1:ptr2+1]
#                 ptr1 = (ptr2+1) if (ptr2+1)<len(s) else ptr2
#                 count =0
        
        # return output
        
        # dictionary to keep track of the number of each characters required
        t_hash = Counter(t)
        
        # required length of the window captured (smallest len)
        required = len(t_hash)
        
        # intialize pointers, counter, output
        ptr1, ptr2 = 0,0
        length_output = float('inf')
        output = ""
        
        # counter would be equal to the unique number of characters in t
        count = 0
        
        # window counter to keep track of chars in window
        window_counts = {}
        
        while ptr2 < len(s):
            # add right ptr character to window
            character = s[ptr2]
            window_counts[character] = window_counts.get(character,0) + 1
            
            # increment count if character occurs the same amount of times in t and window 
            if character in t_hash and (window_counts[character]==t_hash[character]):
                count+=1
            
            while (ptr1 <= ptr2 and count==required):
                character = s[ptr1]
                
                # store minimum window
                if ptr2 - ptr1 < length_output:
                    output = s[ptr1:ptr2+1]
                    length_output = len(output)
                           
                # update window counts 
                window_counts[character]-= 1
                if character in t_hash and window_counts[character] < t_hash[character]:
                    count-=1
                    
                # increment left pointer
                ptr1+=1
            
            # expand the window to the right until smallest window in found
            ptr2+=1
            
        return "" if length_output ==float('inf') else output
        
        

                
                