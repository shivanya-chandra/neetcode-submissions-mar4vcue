class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if len(text1) > len(text2):
        #     n = len(text1)
        #     m = len(text2)
        # else:
        m = len(text1)
        n = len(text2)
        
        grid = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text2[i-1] == text1[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i][j-1], grid[i-1][j])
    
        return grid[n][m]