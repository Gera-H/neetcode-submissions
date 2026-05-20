class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, col = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r,c))
            directions = [(0,1), (0,-1),(1,0),(-1,0)]
            while(q):
                r,c = q.popleft()
                for i,j in directions:
                    if(i+r < 0 or j+c < 0 or i+r >= rows or j+c >= col or grid[r+i][c+j] == "0"):
                        continue
                    q.append((r+i, c+j))
                    grid[r+i][c+j] = "0"

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands+=1
        
        
        return islands


