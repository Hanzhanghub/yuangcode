# coding:utf-8
'''
date:2017/10/9
content:
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), 
find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.
Return the smallest sum of distance. Return -1 if it is not possible.

 Notice
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

Example
Given a grid:
0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), 
the distance that post office to all the house sum is smallest.)
'''

import copy
class Solution(object):
    def build_office(self, grid):
        # special circumstance
        if not grid:
            return -1

        row = len(grid)
        line = len(grid[0])

        # find all the 0 and all the 1
        zero_coor = []
        one_coor = []
        for i in range(row):
            for j in range(line):
                if grid[i][j] == 0:
                    zero_coor.append((i,j))
                if grid[i][j] == 1 :
                    one_coor.append((i,j))

        #
        min_distance = float('inf')

        for each_zero in zero_coor:
            distance = 0

            for each_one in one_coor:
                # print(each_zero)
                # print(each_one)
                if distance == float('inf'):
                    continue
                # 这里要进行深拷贝，进行参数传递
                tmp_grid = copy.deepcopy(grid)
                tmp = self.shortest_path(tmp_grid,each_zero,each_one)
                if tmp == -1:
                    distance = float('inf')
                    continue
                distance += tmp
            # print(distance)
            if distance < min_distance:
                min_distance = distance
        return min_distance


    def shortest_path(self,grid,source,destination):
        row = len(grid)
        line = len(grid[0])

        # coordinate change array
        DIRECTION = 4
        delta_x = [1, 0, 0, -1]
        delta_y = [0, 1, -1, 0]

        # queue
        queue = []
        queue.append(source)
        grid[source[0]][source[1]] = 1  # avoid repeat

        # result declaration
        result = 0

        while queue:
            queue_size = len(queue)

            result += 1
            for turn in range(queue_size):
                pop_coordinta = queue.pop(0)
                for i in range(DIRECTION):
                    next_x, next_y = pop_coordinta[0] + delta_x[i], pop_coordinta[1] + delta_y[i]
                    if self.isNotBound(next_x, next_y, row, line, grid):
                        if grid[next_x][next_y] == 1:
                            if (next_x, next_y) == destination:
                                return result
                        else:
                            grid[next_x][next_y] = 1
                            queue.append((next_x, next_y))
        return -1

    def isNotBound(self, x, y, row, line, grid):
        if x >= 0 and x < row and y >= 0 and y < line and grid[x][y] != 2:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ret = s.build_office([[0, 1, 0, 0, 0],
                          [1, 0, 0, 2, 1],
                          [0, 1, 0, 0, 0]])
    print(ret)


'''
1.思路没问题：计算每一个0到每一个1的距离，取其中最小值。其中计算0到1的最短路径思路和knight shorest path一样。
2.小点需要注意：
    1. 当此0不能到达某个1时，怎么开始下一个0的循环
    2. 当下一个点(next_x,next_y)是0时入队，是1时判断是否是destination
'''



