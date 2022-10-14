class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        steps:
        1. intialize two pointer - at being and end of array
        2. iterate over the array
        3. ith value is zero
            3.1 swap left pointer value and ith value
            3.2 increment i and left pointer
        4. ith value is two
            4.1 sawp right pointer value and ith value
            4.2 decrement right pointer
        5. ith value is one
            5.1 increment i pointer
        6. repeat from step 3
        """
        
        # edge cases
        if not nums:
            return nums
        
        # intialize pointers
        i, left, right = 0, 0, len(nums) - 1 
        
        # function to swap values
        def swap(arr,l,r):
            tmp = arr[l]
            arr[l]=arr[r]
            arr[r]=tmp
            return arr
        
        while i <= right:
            # print(nums)

            # ith values is zero
            if nums[i]==0:
                nums = swap(nums,left,i)
                i+=1
                left+=1
                print(nums)
                
            # ith value is two
            elif nums[i]==2:
                nums = swap(nums,right,i)
                right-=1
            
            # ith value is one
            elif nums[i]==1:
                i+=1
        
        return nums
                
                
            
            
            
            
            