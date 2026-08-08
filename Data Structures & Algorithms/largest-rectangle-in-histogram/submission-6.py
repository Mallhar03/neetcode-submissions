class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = []
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                height_j , index_j = stack.pop()
                left_boundary = stack[-1][1] if stack else -1
                right_boundary = i if i < len(heights) else len(heights)
                width = right_boundary - left_boundary - 1
                res.append(width * height_j)
            stack.append((heights[i],i))
        i,j = 0,stack[-1][1]   
        while stack:
            height_j,index_j = stack.pop()  
            left_boundary = stack[-1][1] if stack else -1
            right_boundary = len(heights)   
            width = right_boundary - left_boundary - 1
            res.append(width * height_j)
        return max(res)