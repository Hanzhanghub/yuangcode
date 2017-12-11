# coding:utf-8
'''
date:2017/10/9
content:
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position, return the length of the route. 
Return -1 if knight can not reached.

Notice
source and destination must be empty.
Knight can not enter the barrier.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
[Idea]

Examples:
In above diagram Knight takes 3 step to reach from (4, 5) to (1, 1)
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1)  as shown in diagram
'''


class Solution(object):
    def knight_shortest_path(self, grid, source, destination):
        # special circumstance
        if not grid:
            return -1

        row = len(grid)
        line = len(grid[0])

        # coordinate change array
        DIRECTION = 8
        delta_x = [1, 1, -1, -1, 2, 2, -2, -2]
        delta_y = [2, -2, 2, -2, 1, -1, 1, -1]

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
                        if (next_x, next_y) == destination:
                            return result
                        else:
                            grid[next_x][next_y] = 1
                            queue.append((next_x,next_y))

        return -1


    def isNotBound(self, x, y, row, line, grid):
        if x >= 0 and x < row and y >= 0 and y < line and grid[x][y] == 0:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ret = s.knight_shortest_path([[0,1,0],
                                  [0,0,1],
                                  [0,0,0]],
                                 (2,0),
                                 (2,2))
    print(ret)
