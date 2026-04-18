class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxRow, maxCol = len(grid),len(grid[0])
        result = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= maxRow or c >= maxCol or grid[r][c] == "0"):
                return
            
            grid[r][c]="0"
            for dr, dc in direction:
                dfs(r + dr, dc + c)
        
        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1
        
        return result
        