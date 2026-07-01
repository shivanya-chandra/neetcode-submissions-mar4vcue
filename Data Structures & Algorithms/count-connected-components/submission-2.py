class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adMap = {i:[] for i in range(n)}
        visited = set()
        connected = 0

        for n1, n2 in edges:
            adMap[n1].append(n2)
            adMap[n2].append(n1)
        
        def dfs(node):
            if node in visited:
                return
     
            visited.add(node)
            for edge in adMap[node]:
                dfs(edge)
        for nodes in range(n):
            if nodes not in visited:
                connected += 1
                dfs(nodes)
        return connected
