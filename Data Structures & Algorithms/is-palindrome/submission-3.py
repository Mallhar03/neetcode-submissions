class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l , r = 0 ,len(s)-1
        while(r>l):
            while not s[l].isalnum() and l<r:
                l += 1
            while not s[r].isalnum() and r>l:
                r -= 1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else : return False    
        return True                