class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direction = [
            (-1, 0), (0, 1), (0, -1), (1, 0),
        ]
        maxRow, maxCol = len(grid),len(grid[0])
        INF = 2147483647
        def bfs(r, c):
            queue = deque([(r, c)])
            visit = [[False] * maxCol for _ in range(maxRow)]
            visit[r][c]= True
            step = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    if grid[row][col] == 0:
                        return step
                    for dr, dc in direction:
                        nr, nc = row + dr, col + dc
                        if ( maxRow > nr >= 0 and maxCol > nc >= 0 and grid[nr][nc] != -1 and not visit[nr][nc]):
                            visit[nr][nc] = True
                            queue.append((nr,nc))
                step+=1
            return INF

        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
