# coding:utf-8

'''
日期：2017年6月16日
内容：给你一个很大的数组，大到你无法使用len()去火的他的长度，即无法通过此种方法得到end。只能通过ArrayReader得到第k个数
'''

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""


class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # 找到可能的伪结点end
        index = 1
        while reader.get(index) < target:
            index *= 2

        start, end = 0, index
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid

        # double check
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return start
        return -1
