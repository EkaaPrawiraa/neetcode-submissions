class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxRow, maxCol = len(grid), len(grid[0])
        maximum = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= maxRow or c >= maxCol or grid[r][c]== 0 ):
                return 0
            grid[r][c]=0
            area = 1
            for dr, dc in direction:
                area += dfs(dr + r, dc + c)
            return area

        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c]==1:
                    maximum = max(dfs(r, c),maximum)
                    
                    

        return maximum
        