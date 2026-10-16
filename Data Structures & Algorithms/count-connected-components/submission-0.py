class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        v = set()
        d = defaultdict(list)
        for u,x in edges:
            d[u].append(x)
            d[x].append(u)
        def dfs(node,v):
            v.add(node)
            for nei in d[node]:
                if nei not in v:
                    dfs(nei,v)
            return 
        for i in range(n):
            if i not in v:
                dfs(i,v)
                count += 1
        return count                 
        