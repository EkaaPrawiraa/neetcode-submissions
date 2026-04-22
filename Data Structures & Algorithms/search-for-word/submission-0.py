class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow, maxCol = len(board), len(board[0])
        visited = [[False for _ in range(maxCol)] for _ in range(maxRow)]

        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or r >=maxRow or c >= maxCol or board[r][c] != word[index] or visited[r][c]):
                return False
                
            visited[r][c]=True
            res = (dfs(r + 1, c, index + 1) or
                   dfs(r - 1, c, index + 1) or
                   dfs(r, c + 1, index + 1) or
                   dfs(r, c - 1, index + 1))
            visited[r][c]=False
            return res

                

        for i in range(maxRow):
            for j in range(maxCol):
                if dfs(i,j,0):
                    return True
        return False