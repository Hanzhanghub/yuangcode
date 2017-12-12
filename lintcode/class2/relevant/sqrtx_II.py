# coding:utf-8

'''
日期：2017年6月29日
内容：实现 float sqrt(float x) 函数，计算并返回 x 的平方根。
'''


class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # 这题只能自己设置精度来求
        # 特殊情况
        if x == 0.0:
            return 0.0
        start = 0.0
        end = x if x > 1.0 else 1.0
        while start + 1e-12 < end:
            mid = (start + end) / 2
            if mid ** 2 <= x - 1e-12:
                start = mid
            elif mid ** 2 >= x + 1e-12:
                end = mid
            # else:
            #     end = mid
            #     break

        # double check
        if start ** 2 <= x:
            return start
        if end ** 2 <= x:
            return end


if __name__ == '__main__':
    s = Solution()
    ret = s.sqrt(21.16)
    print(ret)
