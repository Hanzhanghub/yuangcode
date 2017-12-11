# coding:utf-8

'''
date: 2017/12/1
content:
Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，
where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building.
Buildings may overlap if you see them from far away，find the outline of them。

An outline can be represented by a triple, (start, end, height), 
where start is the start position on x-axis of the outline, 
end is the end position on x-axis and height is the height of the outline.

Building Outline

注意事项
请注意合并同样高度的相邻轮廓，不同的轮廓线在x轴上不能有重叠。

样例
给出三座大楼：
[
  [1, 3, 3],
  [2, 4, 4],
  [5, 6, 1]
]
外轮廓线为：
[
  [1, 2, 3],
  [2, 4, 4],
  [5, 6, 1]
]
'''

class Solution:
    """
    @param: buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):










