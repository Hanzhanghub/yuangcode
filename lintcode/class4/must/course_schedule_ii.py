# coding:utf-8

'''
date:2017/9/25
content:
你需要去上n门九章的课才能获得offer，这些课被标号为 0 到 n-1 。
有一些课程需要“前置课程”，比如如果你要上课程0，你需要先学课程1，我们用一个匹配来表示他们： [0,1]

给你课程的总数量和一些前置课程的需求，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
Example
给定 n = 2, prerequisites = [[1,0]]
返回 [0,1]

给定 n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
返回 [0,1,2,3] or [0,2,1,3]
'''
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    '''超时版本'''
    # def findOrder(self, numCourses, prerequisites):
    #     # return value
    #     results = []
    #     if numCourses == 0:
    #         return results
    #
    #     # 1. make statistics
    #     in_degree = self.helper(numCourses,prerequisites)
    #
    #     # 2.BFS
    #     queue = []
    #     for i in range(numCourses):
    #         if in_degree[i] == 0:
    #             queue.append(i)
    #             results.append(i)
    #
    #     while queue:
    #         pop_num = queue.pop(0)
    #
    #         for j in range(len(prerequisites)):
    #             if pop_num == prerequisites[j][1]:
    #                 l = prerequisites[j][0]
    #                 in_degree[l] -= 1
    #                 if in_degree[l] == 0:
    #                     queue.append(l)
    #                     results.append(l)
    #
    #     if len(results) == numCourses:
    #         return results
    #     else:
    #         return []
    #
    # # helper for statistics
    # def helper(self,num,pre):
    #     in_degree = {}
    #
    #     for i in range(num):
    #         in_degree.setdefault(i,0)
    #
    #     for j in pre:
    #         in_degree[j[0]] += 1
    #     return in_degree


    '''改正版本'''
    def findOrder(self,numCourses, prerequisites):
        results = []
        if numCourses == 0:
            return results

        # 1.make statistics
        statistic_degree = self.statistic_degree(numCourses,prerequisites)

        # 2.BFS
        queue = []
        for i in range(numCourses):
            if statistic_degree['in'][i] == 0:
                queue.append(i)
                results.append(i)

        while queue:
            pop_num = queue.pop(0)

            if pop_num in statistic_degree['out']:
                for point in statistic_degree['out'][pop_num]:
                    statistic_degree['in'][point] -= 1
                    if statistic_degree['in'][point] == 0:
                        queue.append(point)
                        results.append(point)
        # print(results)
        if len(results) == numCourses:
            return results
        else:
            return []

    def statistic_degree(self,num,pre):
        degree_mapping = {'in':{},'out':{}}

        for i in range(num):
            degree_mapping['in'][i] = 0
        for j in pre:
            degree_mapping['in'][j[0]] += 1
            degree_mapping['out'].setdefault(j[1],[])
            degree_mapping['out'][j[1]].append(j[0])
        print(degree_mapping)
        return degree_mapping


if __name__ == '__main__':
    s = Solution()
    # ret = s.findOrder(10, [[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]])
    ret = s.findOrder(1,  [])
    print(ret)


'''
1.为什么会超时？
问题出在“for j in range(len(prerequisites)):...”，因为这个循环将会针对所有的邻接边，所以当在失败的例子中，这样的
邻接边有10000多条，当然会超时。
2.那么怎么改呢？
将统计入度的字典扩展一下，让他成为即统计入度，又统计出度的字典。这样一来在找有依赖边的时候，只需要根据key去找就可以了。
3.套路是什么？
（1）统计出入度，并且使用查询速度快的数据结构
（2）BFS，根据入度为0的点去找依赖他的点，把其入度-1。
'''