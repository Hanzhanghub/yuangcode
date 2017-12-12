# coding:utf-8

'''
日期：2017年6月27日
内容：求某个整数的平方根
http://www.lintcode.com/zh-cn/problem/sqrtx/
'''


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # 处理特殊情况
        if x == 0:
            return 0

        start, end = 1, x  # 最大就应该只到x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                start = mid
            else:
                end = mid

                # double check
        if end ** 2 <= x:
            return end
        if start ** 2 <= x:
            return start


if __name__ == '__main__':
    s = Solution()
    ret = s.sqrt(9)
    print(ret)
