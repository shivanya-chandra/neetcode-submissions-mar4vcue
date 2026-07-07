class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1)
        n = len(s2)
        grid = [[False] * (n+1) for _ in range(m+1)]
        grid[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    continue
                from_s1 = False
                from_s2 = False

                if i>0 and grid[i-1][j] and s3[i+j-1] == s1[i-1]:
                    from_s1 = True
                if j>0 and grid[i][j-1] and s3[i+j-1] == s2[j-1]:
                    from_s2 = True

                grid[i][j] = from_s1 or from_s2
                

        return grid[m][n]


        