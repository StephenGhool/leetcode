class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # intialize pointers
        left = 0
        total = 0
        min_arr = float('inf')
        
        for right in range(len(nums)):
            total += nums[right]
            
            while(total>=target):
                total -= nums[left]
                min_arr = min(min_arr, right - left + 1)
                left+=1
                

                
           
            
        return 0 if min_arr ==float('inf') else min_arr