# coding:utf-8

'''
date:2017/9/28
content:
Description
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 ( the number zero, one, two).
Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2
'''


class Solution(object):
    def zombieInMatrix(self, grid):
        # special
        if not grid:
            return False

        row = len(grid)
        line = len(grid[0])

        # traverse the matrix to push into queue
        queue = []
        for i in range(row):
            for j in range(line):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # BFS
        if not queue:
            return -1

        count = 0
        DIRECTIONS = 4
        delta_x = [1, 0, 0, -1]
        delta_y = [0, 1, -1, 0]
        while queue:
            queue_size = len(queue)
            for inx in range(queue_size):
                pop_coordinate = queue.pop(0)
                for i in range(DIRECTIONS):
                    next_x, next_y = pop_coordinate[0] + delta_x[i], pop_coordinate[1]+delta_y[i]
                    if self.isNotBound(next_x,next_y,row,line,grid):
                        grid[next_x][next_y] = 1
                        queue.append((next_x,next_y))
            count += 1

        # examine whether all the 0 turn to 1
        result = self.examine(row,line,grid,count)
        return result

    def isNotBound(self,x,y,row,line,grid):
        if x >= 0 and x < row and y >= 0 and y < line and grid[x][y] == 0:
            return True
        return False

    def examine(self,row,line,grid,count):
        for i in range(row):
            for j in range(line):
                if grid[i][j] == 0:
                    return -1
        return count - 1 # 减一是因为当所有的0变成1后，还会多一次的入队。


                #     # 1.
                #     visited = [[False if grid[i][j] == 0 else True for j in range(line)] for i in range(row)]
                #
                #     count = 0
                #     for i in range(row):
                #         for j in range(line):
                #             if grid[i][j] == 1:
                #                 self.bfs(i, j, row, line, grid, visited)
                #                 count += 1
                #     # return
                #     for a in range(row):
                #         for b in range(line):
                #             if not visited[a][b]:
                #                 return -1
                #     return count
                #
                # def bfs(self, x, y, row, line, grid, visited):
                #     DIRECTION = 4
                #     delta_x = [1, 0, 0, -1]
                #     delta_y = [0, 1, -1, 0]
                #     queue = [(x, y)]
                #
                #     while queue:
                #         pop_num = queue.pop(0)
                #
                #         for i in range(DIRECTION):
                #             new_x, new_y = pop_num[0] + delta_x[i], pop_num[1] + delta_y[i]
                #             if self.isNotBound(new_x, new_y, row, line, grid, visited):
                #                 visited[new_x][new_y] = True
                #                 queue.append((new_x, new_y))
                #
                # def isNotBound(self, x, y, row, line, grid, visited):
                #     if x >= 0 and x < row and y >= 0 and y < line and grid[x][y] == 0 and not visited[x][y]:
                #         return True
                #     return False


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 1, 2, 0, 2],
            [1, 0, 0, 2, 0],
            [0, 1, 0, 0, 2]]
    ret = s.zombieInMatrix(grid)
    print(ret)
