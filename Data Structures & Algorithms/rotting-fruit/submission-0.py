class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        row = len(grid)
        col = len(grid[0])
        queue = deque()
      
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while fresh>0 and queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()

                for dr,dc in directions:
                    u = r+dr
                    v = c+dc
                    if (u in range(row) and v in range(col)) and (grid[u][v]==1):
                        grid[u][v]=2
                        queue.append((u,v))
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1
                    








        