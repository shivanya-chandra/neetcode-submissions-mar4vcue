class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        self.c = 2
        print(q)
        while q:
            print(q)
            r,c = q.popleft()

            for ud, rl in directions:
                nr = r + ud
                nc = c + rl

                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != 1:
                    continue
                
                
                q.append((nr, nc))
                grid[nr][nc] = grid[r][c] + 1
                self.c = grid[nr][nc]  
                fresh -=1
                             
        if fresh > 0:
            return -1
        return self.c-2

        