class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.total = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0

            if grid[i][j] == "0" or visited[i][j]:
                return 0
    
            
            visited[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.total += 1
                    dfs(i, j)
        return self.total