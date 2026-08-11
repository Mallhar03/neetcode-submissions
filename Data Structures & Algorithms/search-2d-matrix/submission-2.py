class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        m , n = len(matrix) , len(matrix[i])
        start = 0
        end = m*n-1
        while start<=end:
            mid = start + (end-start) // 2
            row = mid//n
            col = mid%n
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                end = mid - 1
            else:
                start = mid + 1
        return False                 
        