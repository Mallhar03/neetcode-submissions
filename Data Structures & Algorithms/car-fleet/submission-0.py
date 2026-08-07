class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_list = []
        stack = []
        for i in range(len(position)):
            pair_list.append((position[i],speed[i]))
        pair_list.sort(key = lambda x: x[0], reverse=True)   # i copied the syntax
        for p,s in (pair_list):
            time = (target - p) / s
            if not stack:
                stack.append((time,p))
            else:
                if time > stack[-1][0]:
                    stack.append((time,p))
        return len(stack)             
            




        