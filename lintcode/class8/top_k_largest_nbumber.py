# coding:utf-8

'''
date: 12/1
content:
在一个数组中找到前K大的数

样例
给出 [3,10,1000,-99,4,100], k = 3.
返回 [1000, 100, 10]
'''

import heapq

class Solution(object):
    def top_k_largest_number(self, nums, k):
        results = []
        # special condition
        if not nums:
            return results

        # 1. a heap to collect the number
        tmp_heap = []
        for item in nums:
            heapq.heappush(tmp_heap, -item)

        while tmp_heap and k > 0:
            results.append(-1 * heapq.heappop(tmp_heap))
            k -= 1
        return results

if __name__ == '__main__':
    a = [3,10,1000,-99,4,100]
    s = Solution()
    ret = s.top_k_largest_number(a, 3)
    print(ret)

'''
1.常规的先用heap存下所有的数， 在这里我用最大堆（存入-item）既能够将最小堆存为最大堆
2.从最大堆里每次pop出一个数，直到添加k个。
'''











