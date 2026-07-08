class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for key in s:
            if key not in s_dict:
                s_dict[key] = 1
            else:
                s_dict[key] += 1    
        t_dict = {}
        for key in t:
            if key not in t_dict:
                t_dict[key] = 1
            else:
                t_dict[key] += 1 
        for key in s_dict:
            if (key not in t_dict) or (s_dict[key] != t_dict[key]) or len(s) != len(t):
                return False          
        return True    