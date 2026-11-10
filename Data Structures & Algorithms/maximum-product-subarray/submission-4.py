class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        lp,rp = 1,1
        max_p = nums[0]
        i,j = 0,n-1
        while i < len(nums) and j >= 0:
            lp *= nums[i]
            rp *= nums[j]
            max_p = max(max_p,max(lp,rp))
            if nums[i] == 0:
                lp = 1
            i += 1    
            if nums[j] == 0:
                rp = 1 
            j -= 1      
        return max_p    

        