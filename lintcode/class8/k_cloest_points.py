# coding:utf-8


'''
date: 2017/11/28
content:
给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。
如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。

样例
给出 points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
返回 [[1,1],[2,5],[4,4]]
'''
"""
Definition for a point.
"""
from math import sqrt
import heapq
import functools

def cmp(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return -1
        else:
            return 1
    else:
        return 1



class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):

        results = []
        # special condition
        if not points:
            return results

        # step 1: Calculate the distance between the point and origin
        # and store it in a hash map: {distance; [[],[],[]]}
        distance_map = {}
        distance_heap = []
        for i in range(len(points)):
            p_x, p_y =  points[i]
            distance = sqrt((p_x - origin.x) ** 2 + (p_y - origin.y) ** 2)
            if distance in distance_map:
                distance_map[distance].append([p_x,p_y])
            else:
                distance_map[distance] = [[p_x, p_y]]
                heapq.heappush(distance_heap, distance)

        # step 2: Find the top k in the distance_map.keys()
        distance_heap = heapq.nlargest(k, distance_heap)
        while len(results) < k:
            tmp = heapq.heappop(distance_heap)
            # get the value from distance_map
            value = distance_map[tmp]
            if len(value) == 1 :
                results.append(value)
            else:
                # sort by the x coordinate
                # value.sort(key=lambda x: x[0])  # This sort method can be replaced by a function
                # sort by the x coordinate, if x coordinates are equal, then sort it by y coordinate
                key = functools.cmp_to_key(cmp)
                value.sort(key=key)
                results += value

        return results[:k]


'''
1.思路：
    （1）计算points中每个点到origin的距离，存到hash表中--{distance: [[p_x, p_y]...[.., ..]]}
    （2）使用heapq中的nsmallest函数，将hash表中的keys()处理成k个最小值
    （3）对k个最小的distance循环，遇到相同的distance的点时，根据x的坐标从小到大选取，x坐标相同则根据y坐标从小到大
         选取
            （1）这里注意复习functools.cmp_to_key()函数，能将函数cmp()转化成key，然后用于sort(key=key)中
'''






















