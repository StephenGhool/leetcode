class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Method 1: Two pointers
        """
        # edge cases
        if len(s) <= 1:
            return len(s)
        
        # length of string
        length = len(s)
        
        # store number of substrings
        result = 0
        
        # pointers declaration
        left, right = 0,0
        
        # odd
        for i, char in enumerate(s):
            while(left >= 0 and right <= length-1):
                if s[left]==s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
            left = right = i
 
        # pointers declaration
        left, right = 0, 1
        
        # even
        for i, char in enumerate(s):
            while(left >= 0 and right <= length-1):
                if s[left]==s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
            
            left, right = i+1, i+2
        
        
        return result
        