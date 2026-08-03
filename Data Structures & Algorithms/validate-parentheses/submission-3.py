class Solution:
    def isValid(self, s: str) -> bool:
        seen = {'(':')','{':'}','[':']'}
        stack = []
        if s[0]==')'or s[0]=='}'or s[0]==']' or s[-1]=='(' or s[-1]=='{' or s[-1]=='[' or len(s)%2 != 0:
            return False
        for c in s:
            if c in ('(','{','['): #google helped me for using in operator
                stack.append(c)
            elif c in (')','}',']'):
                if not stack:
                    return False
                key = stack[-1] # some youtuber told to use this still i used peek()
                if seen[key] == c:
                    stack.pop() 
                else: return False    
        if not stack:
            return True              
        else: return False