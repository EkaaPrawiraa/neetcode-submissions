class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        minutes = 0
        fresh = 0
        maxRow, maxCol = len(grid), len(grid[0])
        direction =[[0,1], [1, 0], [-1, 0], [0, -1]]

        for i in range(maxRow):
            for j in range(maxCol):
                if grid[i][j]==1:
                    fresh +=1
                if grid[i][j]==2:
                    queue.append((i, j))

        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if (row in range(maxRow) and col in range(maxCol) and grid[row][col]==1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
                