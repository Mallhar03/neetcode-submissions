class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited,path = set(),set()
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        def dfs(node,parent):
            visited.add(node)
            for nei in d[node]:
                if nei in visited and nei != parent:
                    return False
                if nei not in visited:    
                    ans = dfs(nei,node)
                    if not ans:
                        return ans
            return True
        ans = dfs(0,None)
        if not ans:
            return ans
        elif len(visited)!=n:
            return False
        else:
            return ans        
                                         
        