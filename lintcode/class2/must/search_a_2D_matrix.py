# coding:utf-8

'''
日期：2017年6月28日
内容：http://www.lintcode.com/zh-cn/problem/search-a-2d-matrix/
'''


class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # 处理特殊情况
        if matrix is None or len(matrix) == 0:
            return False

        # 预处理矩阵matrix,使之成为一个list
        mat_list = []
        for line in matrix:
            mat_list.extend(line)

        start, end = 0, len(mat_list) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mat_list[mid] == target:
                return True
            if mat_list[mid] > target:
                end = mid
            else:
                start = mid

        # double check
        if mat_list[start] == target or mat_list[end] == target:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    ret = s.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 12)
    print(ret)
