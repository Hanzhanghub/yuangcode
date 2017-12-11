# coding:utf-8

'''
date: 2017/11/27
content: 
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

注意事项
我们可以认为1也是一个丑数

样例
如果n = 9， 返回 10
'''
import heapq
class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # special condition
        if n <= 1:
            return 1

        n -= 1
        key = [2, 3, 5]
        ugly_number = []
        for i in range(len(key)):
            heapq.heappush(ugly_number, (key[i], i))

        value = ugly_number[0]
        while n > 0:
            value, level = heapq.heappop(ugly_number)
            while level < 3:
                new_value = value * key[level]
                heapq.heappush(ugly_number, (new_value, level))
                level += 1
            n -= 1
        return value



if __name__ == '__main__':
    n = 9
    s = Solution()
    ret = s.nthUglyNumber(n)
    print(ret)

'''
1. 注意这道题的思路：
    （1）key = [2,3,5]的作用为乘积因子
    （2）ugly_number作为每次去乘因子的数，这里的数的因子也只有2,3,5.
         特别要注意，其规律为，开始时：[2,3,5]，每乘一个数会将最开头的数pop出，即[3,5,4] --> [5,4,6]，
         而到这个时候，由于其为heapq,所以遵循最小堆原则，将变为[4,5,6]...这样接着往下，每次都会弹出这个
         堆中最小的元素。弹到第n个时满足条件。
'''

















