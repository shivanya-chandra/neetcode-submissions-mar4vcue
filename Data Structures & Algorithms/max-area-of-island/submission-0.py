class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        self.total = 0


        def dfs(i,j):
            if i>= len(grid) or j>= len(grid[0]) or i<0 or j<0:
                return 0
            if visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True

            return 1 + dfs(i+1,j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.total = max(self.total, dfs(i,j))
        return self.total


        