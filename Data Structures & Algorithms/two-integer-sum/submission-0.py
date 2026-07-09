class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_list = []
        for i in range (0,len(nums)):
            for j in range (i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    res_list.append(i)
                    res_list.append(j)
        return res_list        

        