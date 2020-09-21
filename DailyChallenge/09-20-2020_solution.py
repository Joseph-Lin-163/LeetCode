class Solution:
    # Note: not my own, but I wouldn't change the implementation either.
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        output=0
        squares=0
        h=len(grid)
        w=len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    start=(j,i)
                elif grid[i][j]==2:
                    end=(j,i)
                elif grid[i][j]==0:
                    squares+=1

        dire=[(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(cur,his):
            nonlocal output
            x,y=cur
            for dx,dy in dire:
                x_=x+dx
                y_=y+dy
                if 0<=x_<w and 0<=y_<h and (x_,y_) not in his and grid[y_][x_]!=-1:
                    if (x_,y_)==end:
                        if len(his)==squares+1:
                            output+=1
                            break
                        else:
                            continue
                    else:
                        dfs((x_,y_),his+[(x_,y_)])

        dfs(start,[start])
        return output
