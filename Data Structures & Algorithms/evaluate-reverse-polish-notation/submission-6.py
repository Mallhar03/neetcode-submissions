
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+','-','*','/'):
                int_token = int(token)
                stack.append(int_token)
            elif token in ('+','-','*','/'):
                first_popped = int(stack.pop())  
                second_popped = int(stack.pop()) 
                if token == '/' : result = int(second_popped / first_popped)
                elif token == '-' : result = second_popped - first_popped
                elif token == '+' : result = second_popped + first_popped
                elif token == '*' : result = second_popped * first_popped
                stack.append(result)
        return stack[-1]        
        