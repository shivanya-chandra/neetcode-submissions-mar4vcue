class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        path = 0
        m = len(matrix)
        n = len(matrix[0])
        grid = [[0] * (n) for _ in range(m)]
        def dfs(i,j):
            best = 1
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            if i>= m or j>=n:
                return 0
            if grid[i][j] != 0:
                return grid[i][j]


            for r, c in directions:
                nr = r + i
                nc = c + j
            
                if 0<=nr<m and 0<=nc<n and matrix[i][j] < matrix[nr][nc]:
                    best = max(best, 1+ dfs(nr, nc))
            grid[i][j] = best
            return best

        for i in range(m):
            for j in range(n):
                path=max(path, dfs(i,j))
        return path

                    

        