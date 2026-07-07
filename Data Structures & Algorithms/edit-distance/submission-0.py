class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2) + 1
        n = len(word1) + 1

        grid = [[0]*(n) for _ in range(m)]

        for i in range(m):
            grid[i][0] = i

        for j in range(n):
            grid[0][j] = j
        
        for i in range(1,m):
            for j in range(1,n):
                if word2[i-1] == word1[j-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = 1+ min(grid[i][j-1], grid[i-1][j], grid[i-1][j-1])
        
        return grid[m-1][n-1]
        