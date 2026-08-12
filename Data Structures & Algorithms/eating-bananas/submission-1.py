class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start , end  = 1 , max(piles) 
        min_k = 0
        while start<=end:
            k = start + (end - start) // 2
            hours = 0 
            for banana in piles:
                hours += (banana + k - 1) // k
            if hours <= h:
                end = k -1
                min_k = k
            elif hours > h:
                start = k + 1
        return min_k            

  