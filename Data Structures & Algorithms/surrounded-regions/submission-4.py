class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 or c ==0 or c == cols -1):
                    q.append((r,c))
                    board[r][c] = "S"
        
        directions = [(1,0), (0,1),(-1,0), (0,-1)]

        while q:
            r,c = q.popleft()
            for ud, rl in directions:
                nr = r + ud
                nc = c + rl
                if nc < 0 or nr < 0 or nr >= rows or nc >= cols:
                    continue
                if board[nr][nc] != "O":
                    continue
                board[nr][nc] = "S"
                q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
                

