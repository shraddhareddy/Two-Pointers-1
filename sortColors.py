class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0:
            return 
        
        low=0
        high=len(nums)-1
        mid=0

        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]= nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
                
        return nums
    
#time complexity -> O(n)
 #space complexity -> O(1)