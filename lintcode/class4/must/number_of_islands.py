#　coding:utf-8

'''
date:2017/9/28
content:
给一个01矩阵，求不同的岛屿的个数。
0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
例如在矩阵：
[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
中有 3 个岛.
'''
class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # special circumstance
        if not grid:
            return 0

        row = len(grid)
        line = len(grid[0])

        # 1.construct a 2D matrix of visited node
        visited = [[False for j in range(line)] for i in range(row)]
        count = 0

        for i in range(row):
            for j in range(line):
                if self.isNotBound(i,j,row,line,grid,visited):
                    visited[i][j] = True
                    # 2.BFS
                    self.bfs(i,j,row,line,grid,visited)
                    count += 1
        return count

    # 2.BFS
    def bfs(self,x,y,row,line,grid,visited):
        DIRECTIONS = 4
        delta_x = [1,0,0,-1]
        delta_y = [0,1,-1,0]
        queue = [(x,y)]
        while queue:
            pop_num = queue.pop(0)
            for i in range(DIRECTIONS):
                next_x, next_y = pop_num[0]+delta_x[i], pop_num[1]+delta_y[i]
                if self.isNotBound(next_x,next_y,row,line,grid,visited):
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))

    # judge whether the coordinate is a boundary
    def isNotBound(self,x,y,row,line,grid,visited):
        if x>=0 and x< row and y>=0 and y<line and grid[x][y] and not visited[x][y]:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ret = s.numIslands([[1]])
    print(ret)


'''
1.矩阵BFS的统计：统计已遍历过的boolean矩阵
2.判断边界，与判断是否开始入队列可以放在一起实现
3.矩阵的BFS，要根据题意考虑四个方向，甚至八个方向（使用变化数组实现）
'''