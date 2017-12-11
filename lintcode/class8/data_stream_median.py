# coding:utf-8

'''
date: 2017/11/30
content:
数字是不断进入数组的，在每次添加一个新的数进入数组的同时返回当前新数组的中位数。

说明
中位数的定义：
中位数是排序后数组的中间值，如果有数组中有n个数，则中位数为A[(n-1)/2]。
比如：数组A=[1,2,3]的中位数是2，数组A=[1,19]的中位数是1。

样例
持续进入数组的数的列表为：[1, 2, 3, 4, 5]，则返回[1, 1, 2, 2, 3]

持续进入数组的数的列表为：[4, 5, 1, 3, 2, 6, 0]，则返回 [4, 4, 4, 3, 3, 3, 3]

持续进入数组的数的列表为：[2, 20, 100]，则返回[2, 2, 20]
'''

import heapq


class Solution:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """

    number = 0
    min_heap, max_heap = [], []

    def get_median(self):
        return -1 * self.max_heap[0]

    def add(self, item):
        if self.number % 2 == 0:
            heapq.heappush(self.max_heap, -item)
        else:
            heapq.heappush(self.min_heap, item)
        self.number += 1

        if not self.min_heap or not self.max_heap:
            return

        if -1 * self.max_heap[0] > self.min_heap[0]:
            small = self.min_heap[0]
            large = -1 * self.max_heap[0]
            heapq.heapreplace(self.max_heap, -small)
            heapq.heapreplace(self.min_heap, large)




    def medianII(self, nums):

        '''
        Solution 3
        '''
        results = []
        for i in range(len(nums)):
            self.add(nums[i])
            results.append(self.get_median())

        return results

        # results = []
        # # special condition
        # if not nums:
        #     return results
        #
        # # construct a heap
        # sort_num = []
        # for i in range(len(nums)):
        #     '''Solution 2'''
            # # step 1: sort the array
            # # get this new number
            # # examin whether it smaller than heap[0]
            # if len(sort_num) == 0:
            #     sort_num.append(nums[i])
            #     results.append(nums[i])
            #     continue
            #
            # # pop the min number in heap to a tmp array
            # tmp = []
            # while sort_num and nums[i] > sort_num[0]:
            #     tmp.append(sort_num.pop(0))
            #
            # if not tmp:
            #     # if num is smaller than heap[0]
            #     # just add this number to the heap -- log(n)
            #     sort_num.insert(0, nums[i])
            # else:
            #     # concantate the tmp + nums[i] + sort_num
            #     tmp.append(nums[i])
            #     sort_num = tmp + sort_num
            #
            # # step 2: find the median
            # median = sort_num[(len(sort_num) - 1) // 2]
            # results.append(median)


            # '''Solution 1'''
            # # add this number to the heap
            # heapq.heappush(sort_num, nums[i])
            #
            # # get the length of the heap
            # length = len(sort_num)
            #
            # # get the length smallest number in the heap
            # tmp = heapq.nsmallest(length, sort_num)
            #
            # # get the median number in tmp
            # median = tmp[(length - 1) // 2]
            # results.append(median)

        # return results


if __name__ == '__main__':
    a = [2,20,13,18,15,8,3,5,4,25]
    s = Solution()
    ret = s.medianII(a)
    print(ret)

'''
1.这道题我自己有三种思路，详细地可见笔记本，但在这里要重点记一下标准答案。
2.这道题的标准答案，可以用于解决求一个乱序数组的中位数的问题。
'''
