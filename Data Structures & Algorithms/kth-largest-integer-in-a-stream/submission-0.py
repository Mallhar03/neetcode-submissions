class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums 
    def add(self, val: int) -> int:
        k_large = self.k
        self.nums.append(val)
        self.nums.sort()
        for i in range(len(self.nums)-1,-1,-1):
            
            if k_large == 1:
                return self.nums[i]
            k_large -= 1    



        
