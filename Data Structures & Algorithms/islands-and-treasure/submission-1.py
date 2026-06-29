from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            r,c = q.popleft()

            for ud, rf in directions:
                nr = r + ud
                nc = c + rf

                if nc < 0 or nr <0 or nr >= len(grid) or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr, nc))
      

