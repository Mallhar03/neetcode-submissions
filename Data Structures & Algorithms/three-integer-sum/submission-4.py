class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        j , k = 1 , len(nums)-1
        res = [] 
        seen = defaultdict(int)
        nums.sort()
        for i in range(len(nums)):
            j = i+1 
            k = len(nums)-1
            while (j<len(nums)and k>=0 and j<k):
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1   
                elif total < 0:
                    j += 1  
                else:
                    add_to_list = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if not seen[add_to_list]:
                        res.append(list(add_to_list))
                        seen[add_to_list] = 1
                    j += 1
                    k -= 1           
        return res            
