# coding:utf-8

'''
date: 2017/10/12
content:
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。
给定一个整数n，返回所有不同的n皇后问题的解决方案。
每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。

样例
对于4皇后问题存在两种解决的方案：
[
    [".Q..", // Solution 1
     "...Q",
     "Q...",
     "..Q."],
    ["..Q.", // Solution 2
     "Q...",
     "...Q",
     ".Q.."]
]
'''


class Solution(object):
    def nQueen(self, n):
        results = []

        # special circumstance
        if not n:
            return [results]

        # visited documentary aboat column
        visited = [0] * n

        # dfs
        self.helper(visited, n, [], results)

        return results

    def helper(self,
               visited,
               n,
               permutation,
               results):

        # recursion exit
        if len(permutation) == n:
            # draw chess board
            results.append(self.drawChessBoard(permutation))
            # results.append(list(permutation))
            return

        #
        for line in range(n):
            # current coordinate
            x = len(permutation)
            y = line

            if not self.check_condition(visited, x, y, permutation):
                continue

            # add action
            visited[y] = 1
            permutation.append(line)

            # recursion
            self.helper(visited, n, permutation, results)

            # remove action: back tracking
            permutation.pop()
            visited[line] = 0

    def check_condition(self, visited, x, y, permutation):
        # examine whethe (x,y) meet the requirement of queen
        if visited[y] == 1:  # this column has been visited by former queen
            return False
        # check for every node in constructed queen list (permutation)
        for node_x in range(len(permutation)):
            node_y = permutation[node_x]
            # check for slide
            if ((x - y) == (node_x - node_y)) or ((x + y) == (node_x + node_y)):
                return False
        return True

    def drawChessBoard(self, permutation):
        '''reconstruct the chess board according to the permutation'''
        '''
        Note that the index in permutation represents the row of a chess,
        and the value in permutation represents the column of a chess
        '''
        chess_board = []
        for row in range(len(permutation)):
            column = permutation[row]
            each_row = []
            for line in range(len(permutation)):
                if line == column:
                    each_row.append('Q')
                else:
                    each_row.append('.')
            chess_board.append(''.join(each_row))
        return chess_board

import os

if __name__ == '__main__':
    s = Solution()
    ret = s.nQueen(6)
    print(ret)
    os.system('pause')





'''
1.完成度很高，一次过，时间要再快
2.最为复杂的部分为弄清楚和找到当前节点的(x,y)坐标以及之前所有的坐标，并进行条件判断。
    具体地，
    (1) 使用列表的索引indx作为行，列表的值作为列
    (2) 每次判断时，由于是对行进行循环，visited里存的是queen已在的列，所以实际上要判断的是斜线的queen
    斜线的判断方法为：正对角线上的坐标差均为x-y,负对角线上的坐标和为x+y
                x-1,y-1     x-1,y+1
                       \   / 
                        x,y
                       /   \                        
                x+1,y-1     x+1,y+1
'''
