class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , 0
        for i in range(len(numbers)):
            while (j<len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                else: j += 1 
            j = i

        