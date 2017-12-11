# coding:utf-8

'''
date: 2017//11/30
content:
Given k sorted integer arrays, merge them into one sorted array.

Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
'''
import heapq


class Solution(object):
    def merge_k_sorted_array(self, arrays):

        results = []
        # special condition
        if not arrays:
            return results

        # construct a min heap
        nums = []
        for array in arrays:
            for number in array:
                heapq.heappush(nums, number)

        # pop the minimum of the heap to the results
        while nums:
            results.append(heapq.heappop(nums))
        return results


if __name__ == '__main__':
    a = [
        [1, 3, 5, 7],
        [2, 4, 6],
        [0, 8, 9, 10, 11]]
    s = Solution()
    ret = s.merge_k_sorted_array(a)
    print(ret)

'''
1. 将所有的arrays中的数全部加到最小堆中
2. 只要最小堆不为空，每次从最小堆中弹出最顶（最小）元素加入results中
'''



