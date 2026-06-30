class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        tMap = {i:[] for i in range(n)}
        # print(tMap)
        visited = set()
        for e, e2 in edges:
            tMap[e].append(e2)
            tMap[e2].append(e)
        
        def dfs(nes,parent):
            if nes in visited:
                return False
            #why do we need this here and not inside the for loop
            visited.add(nes)
            for e in tMap[nes]:
                #shouldn't nes be the parent
                if e == parent:
                    continue
                
                #why do we need this again? if  we already have it above
                if not dfs(e, nes):
                    return False
                # visited.add(e)
            return True
        if not dfs(0,-1):
            return False
        return len(visited) == n
            

        