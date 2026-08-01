class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []
        for s in strs:
            seen[tuple(sorted(s))].append(s)
        for key,value in seen.items():
            res.append(value) 
        return res    
