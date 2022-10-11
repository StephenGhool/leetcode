class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # steps:
        # 1. 
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        # intialize variable
        ptr1 = 0
        max_count = 0
        charset = set()
        
        for ptr2 in range(len(s)):
            while(s[ptr2] in charset):
                charset.remove(s[ptr1])
                ptr1 +=1
                
            charset.add(s[ptr2])
            max_count = max(max_count, ptr2-ptr1+1)
                
        return max_count
        