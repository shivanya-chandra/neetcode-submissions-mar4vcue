class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adMap = {i:[] for i in range(1, len(edges)+1)}
      
        def dfs(node, target, visit):
            if node == target:
                return True

            visit.add(node)
            for nei in adMap[node]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True
            return False

        for n1, n2 in edges:
            if dfs(n1, n2, set()):
                return [n1,n2]
            adMap[n1].append(n2)
            adMap[n2].append(n1)

        