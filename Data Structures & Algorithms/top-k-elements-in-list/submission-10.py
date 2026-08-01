class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        res = []
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            seen[num] += 1
        for key,value in seen.items():
            bucket[value].append(key)
        for i in range (len(bucket)-1,0,-1):
                if not bucket[i]:
                    continue
                else:
                    res.extend(bucket[i]) 
                    if len(res) == k:
                        return res

                    










































