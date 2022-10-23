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
    
#         """
#         Method 2: Two pointers condensed
#         """
        
#         # edge cases
#         if len(s) <= 1:
#             return len(s)
        
#         # store number of substrings
#         result = 0
        
#         # even and odd
#         for i, char in enumerate(s):
#             result += self.countpalindrome(s, i, i)
#             result += self.countpalindrome(s, i, i+1)
        
#         return result
            
#     def countpalindrome(self, s, left, right):
#         result = 0 
#         length = len(s)
#         while(left >= 0 and right <= length-1 and (s[left]==s[right])):
#             result += 1
#             left -= 1
#             right += 1
#         return result
              
        