# coding:utf-8

'''
date: 2017/11/28
content:
每个学生有两个属性 id 和 scores。找到每个学生最高的5个分数的平均值。
'''
import heapq

class Student(object):
    def __init__(self, id, scores):
        self.id = id
        self.scores = scores

class Solution(object):
    def high_five(self, stu):
        top5 = []
        for score in stu.scores:
            if len(top5) < 5:
                heapq.heappush(top5, score)
            else:
                if score > top5[0]:
                    heapq.heappop(top5)
                    heapq.heappush(top5, score)
        sum = 0
        for i in range(len(top5)):
            sum += top5[i]
        return sum / 5

'''
1. 注意一点：heapq自带heapq.nlargest和heapq.nsmallest操作。
'''







