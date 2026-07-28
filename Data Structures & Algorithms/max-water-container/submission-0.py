class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                capacity = (j - i) * min(heights[i],heights[j])
                res.append(capacity)
        return max(res)
        