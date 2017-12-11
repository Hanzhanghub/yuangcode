# coding:utf-8

'''
date: 2017/11/28
content:
实现一个数据结构，提供下面两个接口
1.add(number) 添加一个元素
2.topk() 返回前K大的数

样例
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
'''
import heapq


class Solution(object):
    def __init__(self, k):
        self.topK = []
        self.kContraint = k

    def add(self, num):
        if len(self.topK) < self.kContraint:
            heapq.heappush(self.topK, num)
        else:
            # if self.topK.length == k
            mininum = self.topK[0]
            if num > mininum:
                heapq.heappop(self.topK)
                heapq.heappush(self.topK, num)

    def topk(self):
        return sorted(self.topK, reverse=True)

if __name__ == '__main__':
    s = Solution(3)
    s.add(3)
    s.add(10)
    print(s.topk())
    s.add(1000)
    s.add(-99)
    print(s.topk())
    s.add(4)
    print(s.topk())
    s.add(100)
    print(s.topk())

'''
1.这道题的根本思路在于：维持一个大小为K的最小堆。
2.每次来一个新的num时，如果num <= topK[0], 则丢弃这个num；否则，将topK[0]替换成num，重新进行最小堆的heapify
'''



